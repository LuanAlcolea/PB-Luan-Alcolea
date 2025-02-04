# Exercícios

* [Ir para o script: Geração em massa de dados](https://github.com/LuanAlcolea/PB-Luan-Alcolea/tree/main/Sprint-8/Exercícios/Geração_em_massa_de_dados/Exercício_Geração_em_Massa_de_Dados.py)

* [Ir para o script: Apache Spark](https://github.com/LuanAlcolea/PB-Luan-Alcolea/tree/main/Sprint-8/Exercícios/Apache_Spark/Exercício_Apache_Spark.py)

## Geração em massa de dados
Neste exercício vamos gerar dados que serão utilizados na próxima atividade, o script python deve usar uma biblioteca chamada "nomes" para popular um arquivo de texto com nomes mais utilizados.

### Etapa 1 (warp up):
A primeira etapa eu criei uma função chamada "executar_etapa_1" da qual vai gerar uma lista contendo 250 numeros inteiros obtidos de forma aleatoria, depois aplico a função reverse na lista e imprimo o resultado na tela. Criei uma função auxíliar chamada "generate_random_int" para gerar um número inteiro dentro de dois intervalos de números.

![](/Sprint-8/Evidências/ex_1_et_1.png)

### Etapa 2 (warm up)
Nesta etapa devemos criar uma lista de 20 indices contendo um nome de animal, devemos ordenar a lista de forma crescente e imprimir seus valores usando o "list comprehension", após isso vamos armazenar o conteúdo da lista em um arquivo de texto na extensão CSV. A função "executar_etapa_3" é a responsável por realizar essas operações.

![](/Sprint-8/Evidências/ex_1_et_2.png)

### Etapa 3
Nesta etapa devemos gerar um dataset com nomes de pessoas usando a biblioteca "names". Esta etapa está dividida em 5 passos de execução, a função que vai executar todos os passos se chama "executar_etapa_3".

![](/Sprint-8/Evidências/ex_1_et_3.png)

#### Passo 1:
O primeiro passo é instalar a biblioteca "names" no nosso ambiente de desenvolvimento, para isso devemos executar o seguinte comando: "pip install names". Esta biblioteca será a responsável por trazer dados de nomes ao nosso ambiente.
#### Passo 2:
Após a instalação da biblioteca "names", vamos importar as bibliotecas ao nosso código: "random", "time" e "names".
#### Passo 3:
Agora vamos definir alguns paramêtros que vão nos auxíliar na quantidade de nomes aleatórios e a quantidade de nomes únicos.
#### Passo 4:
Nesta parte vamos gerar os nomes, através de uma função auxíliar eu escrevi o script que vai realizar essa tarefa.
#### Passo 5:
Devemos criar um arquivo de texto contendo todos os nomes aleatórios um a um a cada linha, o nome do arquivo é "nomes_aleatorios.txt".
#### Passo 6:
Verificar o conteúdo do arquivo "nomes_aleatorios.txt".

![](/Sprint-8/Evidências/ex_1_ps_6.png)

## Apache Spark
Neste exercício vamos usar o pyspark para realizar operações sobre o nosso arquivo "nomes_aleatorios.txt", usaremos SQL dentro do pyspark e operações proprias do pyspark para realizar este exercício.

### Etapa 1:
Vamos preparar todo o código para inicializar o pyspark, no meu caso eu usei o google colab para executar o script.

![](/Sprint-8/Evidências/ex_2.png)

Carregaremos o arquivo "nomes_aleatorios.txt" para o nosso ambiente.

![](/Sprint-8/Evidências/ex_2_et_1.png)

### Etapa 2:
Nesta etapa é necessário renomear a coluna gerada automaticamente para "nomes"

![](/Sprint-8/Evidências/ex_2_et_2.png)

### Etapa 3:
Vamos adicionar uma coluna chamada "Escolariedade" e valores os três valores aleatórios que serão atribuidos a cada nome, os valores possíveis são: "Fundamental", "Médio" ou "Superior".

![](/Sprint-8/Evidências/ex_2_et_3.png)

### Etapa 4:
Agora vamos adicionar uma coluna chamada "Pais" da qual vai atribuir de forma aleatória a um nome um dos 13 países da américa do sul.

![](/Sprint-8/Evidências/ex_2_et_4.png)

### Etapa 5:
Adicionar uma coluna chamada "AnoNascimento" com valores aleatórios de 1945 a 2010 para cada nome do dataframe.

![](/Sprint-8/Evidências/ex_2_et_5.png)

### Etapa 6:
Vamos usar o metodo select do dataframe nomes para selecionar as pessoas que nasceram neste século, vamos armazenar o resultado em um outro dataframe chamado "df_select", vamos imprimir os 10 nomes deste dataframe novo.

![](/Sprint-8/Evidências/ex_2_et_6.png)

### Etapa 7:
Vamos executar a mesma tarefa da etapa 6, mas agora usando o Spark SQL.

![](/Sprint-8/Evidências/ex_2_et_7.png)

### Etapa 8:
Vamos usar o metodo filter do dataframe nomes para contar o número de pessoas que fazem parte da geração "Millennials".

![](/Sprint-8/Evidências/ex_2_et_8.png)

### Etapa 9:
Agora vamos realizar o mesmo da etapa 8, porem usando o Spark SQL.

![](/Sprint-8/Evidências/ex_2_et_9.png)

### Etapa 10:
Na última etapa vamos obter a quantidade de pessoas de cada país para cada uma das gerações listadas, que são: "Baby Boomers", "Geração X", "Millennials", "Geração Z". Vamos imprimir em ordem crescente o resultado da consulta, ordenando por Pais, Geraççao e Quantidade, o resultado deve estar em um novo dataframe.

![](/Sprint-8/Evidências/ex_2_et_10.png)
