import csv
import random
import time
import os
import names

# Variáveis auxiliares
#files_path = "Exercícios/Geração_em_massa_de_dados/"
files_path = "C:/Users/Luan/Documents/Compass/PB-Luan-Alcolea/Sprint-8/Exercícios/Geração_em_massa_de_dados/"

def generate_random_int(min, max):
    return random.randint(min, max)


def create_text_file(list, name):
    with open(name, mode='w', newline='') as file:
        output = csv.writer(file)
        for line in list:
            output.writerow([line])


# Etapa 1: gerar uma lista com 250 itens com valores aleatórios
# Após, aplicar a função reverse na lista
def executar_etapa_1():
    min_value = 1
    max_value = 250
    random_list = []

    for i in range(max_value):
        random_list.append(generate_random_int(min_value, max_value))

    random_list.reverse()

    print("Etapa 1 - Imprimindo lista com valores aleatórios de 1 a 250")
    print(random_list)


# Etapa 2: iniciar uma lista com nomes de 20 animais. Ordenar em order crescente,
# Iterar sobre a lista, imprimindo um a um usando o list comprehension, após, 
# armazenar o conteúdo da lista em um arquivo csv.  
def executar_etapa_2():
    animal_list = [
        "Gato", "Cachorro", "Coelho", "Rato", "Ramister",
        "Lobo", "Panda", "Lince", "Tigre", "Coiote",
        "Urso", "Castor", "Girafa", "Morcego", "Galinha",
        "Esquilo", "Pato", "Codorna", "Elefante", "Capivara"   
    ]

    animal_list.sort()

    [print(animal) for animal in animal_list]

    print("Etapa 2 - Salvando lista de animais em um arquivo CSV")

    create_text_file(animal_list, f"{files_path}animals.csv")


# Etapa 3: gerar um dataset com nomes aleatorios de pessoas e salvar os nomes linha por linha 
# em um arquivo chamado "nomes_aleatorios.txt"
def executar_etapa_3():
    # Passo 1: instalar biblioteca "names"
    # Passo 2: Importar random, time, os e names
    # Passo 3: escrever os parâmetros para a geração do dataset
    current_time = time.time()
    random.seed(current_time)

    qtd_nomes_unicos = 3000
    qtd_nomes_aleatorios = 10000000

    # Passo 4: gerar nomes aleatórios
    aux = []

    for i in range(0, qtd_nomes_unicos):
        aux.append(names.get_full_name())
    
    print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

    dados = []

    for i in range(0, qtd_nomes_aleatorios):
        dados.append(random.choice(aux))

    print("Etapa 3 - Gerando arquivo 'nomes_aleatorios.txt'")
    # Passo 5: gerar um arquivo de texto contendo os nomes, um a cada linha
    create_text_file(dados, f"{files_path}nomes_aleatorios.txt")


executar_etapa_1()
executar_etapa_2()
executar_etapa_3()