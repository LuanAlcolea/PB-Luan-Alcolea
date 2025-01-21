import sys
import json
import requests
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # TODO implement

    # S3 functions
    def ConfigureClient(key_id, secret_key_id, token):
        return boto3.client('s3',
                            aws_access_key_id=key_id, 
                            aws_secret_access_key=secret_key_id, 
                            aws_session_token=token,
                            region_name='us-east-1')


    def UploadFileToS3(s3_client, bucket_name, local_file_path, s3_file_path):
            try:
                s3_client.upload_file(local_file_path, bucket_name, s3_file_path)
                print(f'Sucesso ao carregar arquivo no bucket: {bucket_name}')
            except Exception as e:
                print(f'Erro ao carregar arquivo no bucket: {e}')

        
    # API TMDB Functions
    def RequestData(url):
        try:
            response = requests.get(url)
            data = response.json()
        except:
            print("Erro na requisição de dados")
            return None
        return data


    def GetGenreId(genrename):
            url_genres = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
            genres_data = RequestData(url_genres)
            genres = {genre['name']: genre['id'] for genre in genres_data['genres']}
            return genres.get(genrename)


    def GetPopularMoviesByGenres(genre1, genre2, page, filter_both=False):
            start_year = 2000
            end_year = 2022
            start_date = f"{start_year}-01-01"
            end_date = f"{end_year}-12-31"
            
            # Se verdadeiro, buscar filmes que são drama e romance
            if filter_both:
                url_movies = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&sort_by=popularity.desc&with_genres={genre1},{genre2}&primary_release_date.gte={start_date}&primary_release_date.lte={end_date}&page={page}&vote_count.gte=100"
            else:
                # Se não buscar drama ou romance
                url_movies = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&sort_by=popularity.desc&with_genres={genre1}&with_genres={genre2}&primary_release_date.gte={start_date}&primary_release_date.lte={end_date}&page={page}&vote_count.gte=100"
            
            movie_data = RequestData(url_movies)
            return movie_data


    def GetMovieCredits(movie_id):
            url_credits = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language=en-US"
            return RequestData(url_credits)


    def GetMovieDetails(movie_id):
        url_details = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        return RequestData(url_details)

    # Chave da API
    api_key = 'API_KEY'
    if not api_key:
        raise ValueError("API Key incorreta ou não configurada")

    # IDs dos generos dos filmes
    drama_id = GetGenreId("Drama")
    romance_id = GetGenreId("Romance")

    # Inicializar a página
    page = 1
    max_movies = 100
    all_movies = []

    # Buscar filmes de várias páginas do genero drama/romance
    while True:
        if len(all_movies) >= max_movies:
            break
        movie_data = GetPopularMoviesByGenres(drama_id, romance_id, page=page, filter_both=False)
        if not movie_data or "results" not in movie_data or len(movie_data["results"]) == 0:
            break
        
        all_movies.extend(movie_data["results"])
        page += 1

    # Lista para armazenar dados dos filmes de sucesso
    success_movies = []

    # Extrair informações
    for movie in all_movies:
        movie_id = movie["id"]
        movie_name = movie["title"]
        release_date = movie["release_date"]
        rating = movie["vote_average"]
        genre_ids = movie.get("genre_ids", [])

        # Obter id do filme
        movie_details = GetMovieDetails(movie_id)
        imdb_id = movie_details.get("imdb_id", "")

        # Obter o orçamento e a bilheteira
        budget = movie_details.get("budget", 0)
        revenue = movie_details.get("revenue", 0)

        # Obter os nomes dos gêneros
        genres = []
        if drama_id in genre_ids:
            genres.append("Drama")
        if romance_id in genre_ids:
            genres.append("Romance")

        # Obter creditos e membros da equipe do filme
        credits_data = GetMovieCredits(movie_id)
        actors = []
        crew = []
        
        if credits_data:
            if "cast" in credits_data:
                # Ordenar os atores pela popularidade em ordem decrescente
                sorted_actors = sorted(credits_data["cast"], key=lambda x: x["popularity"], reverse=True)
                
                # Extrair os 10 atores populares
                for actor in sorted_actors[:10]:
                    actors.append(actor["name"])
            
            if credits_data and "crew" in credits_data:
                # Extrair os 30 primeiros nomes do time de produção
                limited_crew = credits_data["crew"][:30]
                for member in limited_crew:
                    crew.append({
                        "name": member["name"],
                        "job": member["job"]
                    })

        # Registrar filme se revenue e budget forem existentes
        if revenue and budget > 0:
            success_movies.append({
            "movie_id": imdb_id,
            "movie_name": movie_name,
            "release_date": release_date,
            "rating": rating,
            "budget": budget,
            "revenue": revenue,
            "actors": actors,
            "crew": crew,
            "genres": genres
        })

        # Se houver 100 ou mais registros, interromper
        if len(success_movies) >= max_movies: 
            break

    # Criar JSON com os registros
    output_file = "/tmp/movies_details.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(success_movies, f, ensure_ascii=False, indent=4)

    print(f"Dados salvos em {output_file}")
    
    # Variáveis auxiliares
    year = datetime.now().strftime('%Y')
    month = datetime.now().strftime('%m')
    day = datetime.now().strftime('%d')
    bucket_name = 'data-lake-luan'
    filename = 'movies_details.json'
    s3_path = f'Raw/TMDB/JSON/{year}/{month}/{day}/'

    # Configure s3 client
    s3_client = ConfigureClient('KEY', 'SECRET_KEY', 'TOKEN')
    # Upload json
    UploadFileToS3(s3_client, bucket_name, output_file, f'{s3_path}{filename}')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
