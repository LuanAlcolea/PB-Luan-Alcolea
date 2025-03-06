# Sprint 10
## Resumo da sprint
Está sprint é a ultima do programa de bolsas da trilha de Data & AL da qual vamos encerrar o programa com a entrega do desafio final. A entrega final consiste em desenvolver um dashboard no AWS Quicksight utilizando os dados que preparamos ao longo das sprints anteriores, devemos utilizar o AWS Glue Data Catalog para gerar as tabelas que serão utilizadas nas consultas no AWS Athena. A construção do dashboard envolve as etapas de planejamento e preparação dos dados, devemos começar definindo o que queremos representar em nosso dashboard, com isso definido devemos extraír, processar e preparar os dados no data lake a serem utilizados pelo AWS Quicksight.

A entrega deste desafio final é realizada em um vídeo de 12 a 15 minutos da qual vai abordar tudo sobre o desafio final, desde as implementações dos scripts até as mais diversas dificuldades encontradas. Esta documentação conterá todas as etapas que eu vivenciei para alcançar o resultado final do desafio, desde as primeiras implementações, até as ultimas mudanças bruscas nos scripts e da analise final.

## Resumo do desafio final
Para iniciar o desafio devemos criar um Bucket no AWS S3, que será utilizado como o nosso data-lake, o primeiro passo a ser executado é trazer os dados sem tratamentos de duas origens diferentes. 

A primeira origem é a local, um script python será desenvolvido para ser executado dentro de um container no Docker para carregar os arquivos CSVs para a camada Raw. Posteriormente vamos desenvolver um script python que será executado no AWS Lambda que carregará dados da API TMDB e IMDB para a camada Raw.

Com os dados presentes no data-lake, é momento de processar e converter os dados para serem armazenados na camara Trusted. Um script python que será executado no AWS Glue será desenvolvido para este fim, os dados de formatos diferentes serão limpos e convertidos para Parquet.

Neste momento desenvolvemos a modelagem de dados que será estruturada conforme o objetivo final da analise individual. A modelagem deve ser capaz de estabelecer as relações entre as tabelas e responder as questões definidas previamente. As tabelas devem ser geradas a partir de um script python que será executado no AWS Glue e será armazenada na camada Refined.

Com as tabelas presentes na camada Refined do data-lake, é momento de desenvolver o dashboard, planejar, prototipar e criar. Vamos utilizar o AWS Glue Data Catalog para criar o banco de dados que será utilizado pelo AWS Athena para realizar consultas. Com os dados prontos a serem utilizados, começamos o desenvolvimento do dashboard, vamos estabelecer qual será o objetivo final do dashboard e como esse objetivo será alcançado. Vamos preparar um storytelling para ser capaz de trazer valores ao dashboard apresentado.

O dashboard é desenvolvido utilizando o AWS Quicksight, da qual permite a fácil manipulação de dados nos gráficos e tabelas. Os dados todos serão oriundos do AWS Athena, podemos desenvolver Views para facilitar ou utilizar os dados das tabelas previamentes criadas.

## Desafio

Antes de iniciar o desafio, eu reorganizei os dados do data lake, ajustei os scripts do AWS Lambda e Glue, bem como re-executei todos eles para garantir que os dados estejam consistentes. A modelagem de dados entregue na sprint 9 apresentava irregulariedades, então nesta sprint eu ajustei todos os problemas da modelagem e das questões que eu vou responder no dashboard.

O objetivo do meu dashboard é extraír insights importantes utilizando como base os dados de filmes produzidos, atores que participaram e diretores que direcionaram os filmes. Com os dados preparados, iniciei o desenvolvimento do dashboard no AWS Quicksight. Para auxiliar nos dados dispostos nos gráficos eu desenvolvi Views no AWS Athena, ao todo foram oito views desenvolvidas, cada uma para responder uma questão preparada. Eu inclui gráficos de indicadores de KPIs, estes eu optei por utilizar os dados do conjunto de dados não oriundos de views do Athena.

* [Acessar desafio](https://github.com/LuanAlcolea/PB-Luan-Alcolea/tree/main/Sprint-10/Desafio/README.MD)

## Evidências
Esta parte deste documento contém evidências de execução do desafio final.

* Conjunto de dados utilizados no AWS Quicksight
![](/Sprint-10/Evidências/Conjunto_dados.png)

* Visão geral do dashboard no AWS Quiksight
![](/Sprint-10/Evidências/Visão_Quicksight.png)

* Crawler criado no AWS Glue
![](/Sprint-10/Evidências/Crawler.png)

* Banco de dados e as tabelas no AWS Glue Data Catalog
![](/Sprint-10/Evidências/Database.png)

* Visão dos scripts revisados para o desafio final
![](/Sprint-10/Evidências/Visão_novos_script_glue.png)

* Politica de permissões necessárias para o desenvolvimento do desafio final
![](/Sprint-10/Evidências/Permissões.png)


* [Acessar evidências](https://github.com/LuanAlcolea/PB-Luan-Alcolea/tree/main/Sprint-10/Evidências/README.MD)

## Informações afins
Nesta sprint houve um curso que foi realizado na plataforma Udemy, bem como um breve link que explica como desenvolver um dashboard de forma eficiênte. Há também materiais opcionais, neste caso é o AWS Quicksight lab presente nas explicações da entrega final da sprint 10.

## Agradecimentos
Eu sou muito grato a toda equipe da Compass por ter disponibilizado esta oportunidade de estágio para nós realizarmos. Durante todos esses meses eu pude crescer pessoalmente e profissionalmente. Sou grato aos monitores que nós ajudaram a alcançar os objetivos de cada sprint, ao avaliador de nossas documentações e a scrum master que esteve conosco todos os dias, desde o início do estágio até o último dia.