
# === Exercício ETL === #

def abrir_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        return linhas


def get_coluna(arquivo, indice_coluna):
    coluna = []

    for linha in arquivo[1::]:
            dados = []
            valor_atual = ''
            dentro_aspas = False

            for char in linha.strip():
                if char == ',' and not dentro_aspas:
                    dados.append(valor_atual)
                    valor_atual = ''
                elif char == '"':
                    dentro_aspas = not dentro_aspas
                else:
                    valor_atual += char

            dados.append(valor_atual)

            if(len(dados) > indice_coluna):
                coluna.append(dados[indice_coluna])
    
    return coluna
    

# Etapa 1
def get_ator_com_mais_filmes(arquivo):
    coluna_number_of_movies = get_coluna(arquivo, indice_number_of_movies)
    coluna_actor = get_coluna(arquivo, indice_actor)

    valor_maximo = max(coluna_number_of_movies)
    indice = coluna_number_of_movies.index(valor_maximo)

    print(f"Ator/Atriz com maior numero de filmes: {coluna_actor[indice]} : {valor_maximo}")


# Etapa 2
def get_media_gross(arquivo):
    coluna_total_gross = get_coluna(arquivo, indice_total_gross)
    valor = 0.0

    for i in coluna_total_gross:
        valor += float(i)

    if len(coluna_total_gross) > 0:
        media = round(valor / len(coluna_total_gross), 2)
    else:
        media = 0
    
    print(f"Media da receita bruta - {media}")


# Etapa 3
def get_ator_maior_media_por_filme(arquivo):
    coluna_average_per_movie = get_coluna(arquivo, indice_average_per_movie)
    coluna_actor = get_coluna(arquivo, indice_actor)

    coluna_average_per_movie = [float(valor) for valor in coluna_average_per_movie]

    valor_maximo = max(coluna_average_per_movie)
    indice = coluna_average_per_movie.index(valor_maximo)

    print(f"Ator/Atriz com maior media por filme: {coluna_actor[indice]} : {valor_maximo}")


# Etapa 4
def get_filme_mais_repetido(arquivo):
    coluna_movies = get_coluna(arquivo, indice_movie)
    
    contagem_fimes= {}
    
    for filme in coluna_movies:
        if filme in contagem_fimes:
            contagem_fimes[filme] += 1
        else:
            contagem_fimes[filme] = 1
    
    filmes_ordenados = sorted(contagem_fimes.items(), key=lambda x: (-x[1], x[0]))

    i = 0
    for filme, contagem in filmes_ordenados:
        i += 1
        print(f"{i} - O filme {filme} aparece {contagem} vezes no dataset")


# Etapa 5
def get_autor_maior_receita_bruta(arquivo):
    coluna_actor = get_coluna(arquivo, indice_actor)
    coluna_total_gross = get_coluna(arquivo, indice_total_gross)

    actor_gross = []

    for i in range(len(coluna_actor)):
        actor_gross.append((coluna_actor[i], coluna_total_gross[i]))
    
    lista_ordenada = sorted(actor_gross, key=lambda x: x[1], reverse=True)

    for actor, gross in actor_gross:
        print(f"{actor} - {gross}")


# Variáveis globais
arquivo = abrir_arquivo('actors.csv')
indice_actor = 0
indice_total_gross = 1
indice_number_of_movies = 2
indice_average_per_movie = 3
indice_movie = 4

# Execução das etapas
get_ator_com_mais_filmes(arquivo)        # Etapa 1
get_media_gross(arquivo)                 # Etapa 2
get_ator_maior_media_por_filme(arquivo)  # Etapa 3
get_filme_mais_repetido(arquivo)         # Etapa 4
get_autor_maior_receita_bruta(arquivo)   # Etapa 5
