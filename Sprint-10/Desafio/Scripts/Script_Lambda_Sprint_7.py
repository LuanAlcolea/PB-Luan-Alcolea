import json
import os
import requests
import boto3
import concurrent.futures
from datetime import datetime

# Variáveis Globais
api_key = os.getenv("API_KEY")
bucket_name = 'data-lake-luan'
year = datetime.now().strftime('%Y')
month = datetime.now().strftime('%m')
day = datetime.now().strftime('%d')

# Funções S3
def ConfigureClient():
    return boto3.client('s3',
                        aws_access_key_id = os.getenv("AWS_KEY"),
                        aws_secret_access_key = os.getenv("AWS_SECRET_KEY"),
                        aws_session_token = os.getenv("AWS_TOKEN"),
                        region_name='us-east-1')


def UploadFileToS3(s3_client, bucket_name, local_file_path, s3_file_path):
    try:
        s3_client.upload_file(local_file_path, bucket_name, s3_file_path)
        print(f'Sucesso ao carregar arquivo no bucket: {bucket_name}')
    except Exception as e:
        print(f'Erro ao carregar arquivo no bucket: {e}')


# Funções API TMDB
def RequestData(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erro na requisição: {url} -> {e}")
        return None


def GetMovieData(movie_id):
    # Uso mais workers para acelerar a velocidade de requisições
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_details = executor.submit(GetMovieDetails, movie_id)
        future_credits = executor.submit(GetMovieCredits, movie_id)

        movie_details = future_details.result()
        credits_data = future_credits.result()

    return movie_details, credits_data


def GetMovieCredits(movie_id):
    url_credits = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language=en-US"
    return RequestData(url_credits)


def GetMovieDetails(movie_id):
    url_details = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    movie_details = RequestData(url_details)
    return movie_details


def GetPersonDetails(person_id, cache):
    if person_id in cache:
        return cache[person_id]

    url_person = f"https://api.themoviedb.org/3/person/{person_id}?api_key={api_key}&language=en-US"
    details = RequestData(url_person)
    cache[person_id] = details or {}
    return cache[person_id]


def GetPersonDetailsConcurrently(person_ids, cache):
    person_details_list = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(GetPersonDetails, person_id, cache) for person_id in person_ids]
        for future in concurrent.futures.as_completed(futures):
            person_details_list.append(future.result())
    return person_details_list


def lambda_handler(event, context):
    global api_key, bucket_name, year, month, day

    # Inicializar variáveis
    page = 1
    max_movies = 2500
    all_movies = []
    current_json = 0
    person_cache = {}

    allowed_genre_names = {'Drama', 'Romance'}

    # Buscar filmes populares
    while len(all_movies) < max_movies:
        url_movies = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US&sort_by=popularity.desc&primary_release_date.gte=1960-01-01&primary_release_date.lte=2022-12-31&page={page}&with_genres=18,10749"
        movie_data = RequestData(url_movies)

        if not movie_data or not movie_data.get("results"):
            print(f"Nenhum filme retornado na página {page}. Interrompendo busca.")
            break

        all_movies.extend(movie_data.get("results", []))

        if len(movie_data.get("results", [])) < 20:
            print(f"Menos de 20 filmes retornados na página {page}, assumindo ser a última página.")
            break

        page += 1
        if page > 50:
            print("Limite de páginas atingido. Interrompendo busca.")
            break


    # Lista para armazenar dados dos filmes processados
    success_movies = []

    # Processamento dos filmes
    for movie in all_movies:
        movie_id = movie["id"]
        movie_name = movie["title"]
        release_date = movie.get("release_date", "")

        movie_details, credits_data = GetMovieData(movie_id)

        if not movie_details:
            continue

        movie_genres = {genre['name'] for genre in movie_details.get('genres', [])}
        if not allowed_genre_names.intersection(movie_genres):
            continue

        imdb_id = movie_details.get("imdb_id", "")
        budget = movie_details.get("budget", 0)
        revenue = movie_details.get("revenue", 0)
        popularity = movie_details.get("popularity", "N/A")
        genres = list(movie_genres)

        actors, actor_ids = [], []
        directors, director_ids, director_genders = [], [], []

        if credits_data:
            actor_credits = credits_data.get("cast", [])[:9]
            director_credits = credits_data.get("crew", [])

            actor_person_ids = [actor["id"] for actor in actor_credits]
            director_person_ids = [member["id"] for member in director_credits if member["job"] == "Director"]

            all_person_ids = list(set(actor_person_ids + director_person_ids))

            person_details_results = GetPersonDetailsConcurrently(all_person_ids, person_cache)
            person_details_dict = {details['id']: details for details in person_details_results if details}

            for actor in actor_credits:
                actor_id = actor["id"]
                actor_details = person_details_dict.get(actor_id, {})

                actors.append(actor["name"])

            for member in director_credits:
                if member["job"] == "Director":
                    director_id = member["id"]
                    director_details = person_details_dict.get(director_id, {})

                    directors.append(member["name"])
                    director_genders.append(director_details.get("gender", "N/A"))

        if revenue and budget > 0:
            success_movies.append({
                "movie_id": imdb_id,
                "movie_name": movie_name,
                "release_date": release_date,
                "budget": budget,
                "revenue": revenue,
                "popularity": popularity,
                "genres": genres,
                "actors": actors,
                "directors": directors,
                "director_genders": director_genders,
            })

        # Salvar em arquivos JSON a cada 100 filmes
        if len(success_movies) >= 100:
            current_json += 1
            local_path = f'/tmp/tmdb_data_{current_json}.json'
            with open(local_path, 'w', encoding='utf-8') as f:
                json.dump(success_movies, f, ensure_ascii=False, indent=4)

            # Upload para S3
            s3_client = ConfigureClient()
            s3_file_path = f'Raw/TMDB/JSON/{year}/{month}/{day}/tmdb_data_{current_json}.json'
            UploadFileToS3(s3_client, bucket_name, local_path, s3_file_path)

            success_movies = []

    # Salvar novo json
    if success_movies:
        current_json += 1
        local_path = f'/tmp/tmdb_data_{current_json}.json'
        with open(local_path, 'w', encoding='utf-8') as f:
            json.dump(success_movies, f, ensure_ascii=False, indent=4)

        # Upload para S3
        s3_client = ConfigureClient()
        s3_file_path = f'Raw/TMDB/JSON/{year}/{month}/{day}/tmdb_data_{current_json}.json'
        UploadFileToS3(s3_client, bucket_name, local_path, s3_file_path)

    return {
        'statusCode': 200,
        'body': json.dumps('Processamento concluído com sucesso!')
    }