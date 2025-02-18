# Este script representa a segunda implementação da extração de dados da api tmdb
import json
import requests
import boto3
import concurrent.futures
from datetime import datetime

# Variáveis Globais
api_key = 'TMDB_KEY'
bucket_name = 'data-lake-luan'
year = datetime.now().strftime('%Y')
month = datetime.now().strftime('%m')
day = datetime.now().strftime('%d')

# Funções S3
def ConfigureClient():
    return boto3.client('s3',
                        aws_access_key_id="KEY", 
                        aws_secret_access_key="SECRET_KEY", 
                        aws_session_token="TOKEN",
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
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
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
    return RequestData(url_details)


def GetPersonDetails(person_id, cache):
    if person_id in cache:
        return cache[person_id]
    
    url_person = f"https://api.themoviedb.org/3/person/{person_id}?api_key={api_key}&language=en-US"
    details = RequestData(url_person)
    cache[person_id] = details or {}
    return cache[person_id]


# Handler da função Lambda
def lambda_handler(event, context):
    global api_key, bucket_name, year, month, day

    # Inicializar variáveis
    page = 1
    max_movies = 500
    all_movies = []
    current_json = 0
    person_cache = {}

    # Buscar filmes populares
    while len(all_movies) < max_movies:
        url_movies = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US&sort_by=popularity.desc&primary_release_date.gte=1950-01-01&primary_release_date.lte=2022-12-31&page={page}"
        movie_data = RequestData(url_movies)
        
        all_movies.extend(movie_data["results"])
        page += 1

    # Lista para armazenar dados dos filmes processados
    success_movies = []

    # Processamento dos filmes
    for movie in all_movies:
        movie_id = movie["id"]
        movie_name = movie["title"]
        release_date = movie.get("release_date", "")

        # Buscar detalhes e créditos do filme
        movie_details, credits_data = GetMovieData(movie_id)
        
        if not movie_details:
            continue

        imdb_id = movie_details.get("imdb_id", "")
        budget = movie_details.get("budget", 0)
        revenue = movie_details.get("revenue", 0)
        popularity = movie_details.get("popularity", "N/A")
        rating = movie_details.get("vote_average", 0)

        actors, actor_ids, actor_genders, personagens = [], [], [], []
        directors, director_ids, director_genders = [], [], []

        if credits_data:
            for actor in credits_data.get("cast", [])[:15]:
                actor_id = actor["id"]
                actor_details = GetPersonDetails(actor_id, person_cache)

                actors.append(actor["name"])
                actor_genders.append(actor_details.get("gender", "N/A"))
                personagens.append(actor.get("character", ""))

            for member in credits_data.get("crew", []):
                if member["job"] == "Director":
                    director_id = member["id"]
                    director_details = GetPersonDetails(director_id, person_cache)

                    directors.append(member["name"])
                    director_genders.append(director_details.get("gender", "N/A"))

        if revenue and budget > 0:
            success_movies.append({
                "movie_id": imdb_id,
                "movie_name": movie_name,
                "release_date": release_date,
                "rating": rating,
                "budget": budget,
                "revenue": revenue,
                "popularity": popularity,
                "actors": actors,
                "actor_genders": actor_genders,
                "directors": directors,
                "director_genders": director_genders,
                "personagens": personagens
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

            print(f"Novo JSON {current_json} salvo em {local_path}")
            success_movies = []

    # Salvar arquivo
    if success_movies:
        current_json += 1
        local_path = f'/tmp/tmdb_data_{current_json}.json'
        with open(local_path, 'w', encoding='utf-8') as f:
            json.dump(success_movies, f, ensure_ascii=False, indent=4)

        # Upload para S3
        s3_client = ConfigureClient()
        s3_file_path = f'Raw/TMDB/JSON/{year}/{month}/{day}/tmdb_movie{current_json}.json'
        UploadFileToS3(s3_client, bucket_name, local_path, s3_file_path)

        print(f"Novo JSON {current_json} salvo em {local_path}")

    return {
        'statusCode': 200,
        'body': json.dumps('Processamento concluído com sucesso!')
    }
