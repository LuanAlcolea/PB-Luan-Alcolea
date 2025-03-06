# Desafio final
O desafio final consiste em desenvolver o dashboard no AWS Quicksight utilizando puramente os dados que estão presentes em nosso data-lake, na camada refined. Para realizar a última etapa é necessário que os passos anteriores estejam todos corretos, os dados devem estar armazenados e organizados de forma correta, a modelagem e a analise final devem fazer sentido e estarem totalmente prontas. Somente depois de tudo pronto que podemos desenvolver o dashboard final.
## Questões que serão respondidas no dashboard

* 1.Quais diretores mais produziram filmes?

* 2.Quais atores mais atuaram em filmes?

* 3.Qual é a quantidade de filmes produzidos por diretores mulheres em comparação com filmes produzidos por diretores homens?

* 4.Qual a quantidade de filmes lançados dos generos drama e romance ao longo dos anos?

* 5.Relação entre orçamento e popularidade dos filmes;

* 6.Quantidade total de filmes de drama e romance;

* 7.Quais diretores também atuaram?

* 8.Quais filmes com baixo orçamento tiveram grande sucesso de bilheteria?

## Modelagem de dados
![](/Sprint-10/Desafio/Modelagem_de_dados.png)

## Etapa 1 (Sprint 6)
A primeira etapa consistem em carregar os dados de origem local para a camara Raw do data-lake, os dados são dois arquivos do formato CSVs chamados "movies.csv" e "series.csv". Os dados serão armazenados nos diretórios correspondentes dentro do AWS S3. Nesta etapa também vamos decidir quais questões vamos responder na última etapa.

* data-lake/Raw/Local/CSV/Movies/Ano/Mes/Dia/movies.csv;
* data-lake/Raw/Local/CSV/Series/Ano/Mes/Dia/movies.csv;

O processo envolvido nesta etapa é desenvolver um script python e uma imagem docker, o script python deverá ser executado dentro da imagem docker da qual será o responsável por armazenar temporariamente os arquivos do computador local para o container docker. O script utilizará a biblioteca "boto3" para carregar os dados do container para o AWS S3.

### Passo a passo de execução:

* Criei um bucket no AWS S3 chamado "data-lake-luan", é neste bucket em que todos os dados serão armazenados, processados e consumidos;

* Programei o script python que irá carregar os arquivos CSVs que está presente no container para a camada Raw do data-lake;

* Escrevi as instruções de criação de imagem docker que será utilizado;

* Eu executei as etapas necessárias, instanciei um novo container de nossa imagem previamente criada, esse container vai executar o script python que utilizará da biblioteca "boto3" para carregar os dados do container para o AWS S3.

Após as execuções os arquivos CSVs estarão corretamentes carregados no data-lake conforme o esperado;

## Etapa 2 (Sprint 7)
A segunda etapa consiste em extraír dados da API TMDB e IMDB para alimentar de novos dados o nosso data-lake. Vamos decidir primeiramente quais dados vamos utilizar para responder as questões definidas e então buscar esses dados da API, os dados novos tem que ser únicos, não podendo ser os mesmos presentes nos arquivos de dados CSVs. Os arquivos devem ser armazenados na camada Raw seguindo este padrão:
* data-lake/Raw/TMDB/JSON/Ano/Mes/Dia/Arquivos.json;

Para desenvolver esta etapa vamos criar um script python que será executado no AWS Lambda, da qual vai buscar os dados da API e armazenar diretamente no bucket. Eu reformulei o script para que ele extraía alguns dados diferentes conforme a minha analise.

### Passo a passo de execução:
* Antes de começar o desenvolvimento do script eu decidi quais dados eu irei extraír da API;

* Após ter definido quais dados eu vou extraír, eu programei o script python no AWS Lambda e configurei as bibliotecas necessárias;

* Iniciei a execução do script, que vai então gerar arquivos JSON contendo cada um no máximo 100 registros;

Após as execução do script, alguns arquivos JSON foram criados e armazenados na camara Raw do data-lake;

![](/Sprint-10/Evidências/Novo_json.png)

* [Acessar script revisado da sprint 7](https://github.com/LuanAlcolea/PB-Luan-Alcolea/blob/main/Sprint-10/Desafio/Scripts/Script_Lambda_Sprint_7.py)

## Etapa 3 (Sprint 8)
A terceira etapa do desafio é processar os arquivos previamentes carregados, limpandos seus dados e convertendo eles para um formato único de arquivo chamado "Parquet".

Será desenvolvido dois scripts python que será executado no AWS Glue será desenvolvido para esta tarefa, um script vai ler os arquivos CSVs da camada Raw, vai limpar os dados, converter para "Parquet" e armazenar na camada Trusted. Os caminhos do S3 são esses:

* data-lake/Trusted/Local/Parquet/Movies/Arquivos.parquet;
* data-lake/Trusted/Local/Parquet/Series/Arquivos.parquet;
* data-lake/Trusted/TMDB/Parquet/Movies/Ano/Mes/Dia/movies_parquet/Arquivos.parquet;

### Passo a passo de execução:
* Eu desenvolvi primeiramente o script de conversão dos arquivos CSVs, eu executei eles e os novos arquivos foram gerados com sucesso;
* Posteriormente eu escrevi o script de conversão de JSON para Parquet, neste script eu modifiquei bastante vezes para que ele siga os conformes de minha analise;

Após as execuções os arquivos convertidos e limpos são persistidos na camada Trusted.

* [Acessar script revisado da sprint 8](https://github.com/LuanAlcolea/PB-Luan-Alcolea/blob/main/Sprint-10/Desafio/Scripts/Script_Glue_Sprint_8.py)

## Etapa 4 (Sprint 9)
A quarta etapa do desafio consiste em desenvolver a modelagem dos dados multidimensional e refinar os dados. Vamos criar um script que vai criar as tabelas de dados, os dados são extraídos dos parquets gerados na etapa anterior.

### Passo a passo de execução:

* Desenvolvi a modelagem de dados utilizando a ferramenta "draw.io", a primeira implementação que foi nesta sprint 9 houve alguns problemas nas disposições das tabelas de dados.

* Com a modelagem pronta, eu escrevi o script python no AWS Glue que vai extraír os dados das duas origens diferentes e vai compor os dados conforme a modelagem.

* Após os dados prontos na camada refined, eu criei um banco de dados no AWS Glue, criei um Crawler e executei, eu verifiquei a integridade dos dados presentes nas tabelas da refined utilizando o AWS Athena.

* [Acessar script revisado da sprint 9](https://github.com/LuanAlcolea/PB-Luan-Alcolea/blob/main/Sprint-10/Desafio/Scripts/Script_Glue_Sprint_9.py)

## Etapa 5 (Sprint 10)

### Ajuste na modelagem de dados
* Quando a sprint 10 iniciou, eu me deparei com alguns problemas na minha modelagem de dados e nos dados que estavam presentes no data-lake. Por esse motivo eu comecei a sprint ajustando a modelagem de dados e a minha analise.

### Reingestão de dados da API TMDB
#### Sprint 7
* Com as mudanças recentes da analise e da modelagem, surge a necessidade de eu ajustar os scripts de ingestão, processamento e preparação dos dados. Comecei pelo script no AWS Lambda, realizei a ingestão de dados corretamente, seguindo a minha modelagem de dados. 
#### Sprint 8
* Com os dados da camada Raw agora prontos, ajustei o script no AWS Glue de conversão de formatos e limpeza de dados. Os dados novos estão corretamentes estruturados e organizados na camada Trusted.
#### Sprint 9
* Em seguida eu ajustei o script de refinamento dos dados, agora o script é capaz de gerar as tabelas corretamente. A versão anterior entregue na sprint 9 havia um problema com a dimensão atores, da qual a geração dos IDs estava com erros, o que impossibilitava de ser utilizados no AWS Quicksight.

#### Visão do Crawler criado
![](/Sprint-10/Evidências/Crawler.png)

#### Visão das tabelas e views criadas
![](/Sprint-10/Evidências/Database.png)

### Desenvolvimento do dashboard
#### Preparação dos conjunto de dados
* Antes de iniciar a construção do dashboard, eu desenvolvi oito views no AWS Athena que vai auxíliar na construção da maioria dos gráficos. Para cada view criada, foi criado um conjunto de dados no Quicksight, e carregados na analise final.

* [Acessar as consultas desenvolvidas para cada views](https://github.com/LuanAlcolea/PB-Luan-Alcolea/blob/main/Sprint-10/Desafio/Scripts/Views_Athena.md)

#### Construção do dashboard
Durante a criação dos conjuntos de dados, houve um erro de permissão que a AWS mostrou em tela, para resolver este problema eu tive que ir no AWS IAM e adicionar novas politicas de permissões ao meu usuário.

![](/Sprint-10/Evidências/Permissões.png)

O desenvolvimento se iniciou criando os gráficos para responder as minhas questões. 

* O primeiro gráfico desenvolvido foi um gráfico de rosca, da qual apresenta valores em porcentagem, incluindo o valor total no meio. A pergunta respondida foi: Qual é a quantidade de filmes produzidos por diretores mulheres em comparação com filmes produzidos por diretores homens?
![](/Sprint-10/Evidências/Gráfico_1.png)

* O segundo gráfico também é um gráfico de rosca, e busca responder da mesma forma da anterior a seguinte pergunta: Quantidade total de filmes de drama e romance;
![](/Sprint-10/Evidências/Gráfico_2.png)

* O terceiro gráfico é um de rosca, como as duas primeiras. Busca responder a seguinte questão: Obras que os diretores também atuaram;
![](/Sprint-10/Evidências/Gráfico_3.png)

* O quarto gráfico é um de nuvem, em que apresenta uma série de nomes de varios tamanhos e posições, incluindo posições verticais. A pergunta que este gráfico responde é: Quais atores mais atuaram em filmes?
![](/Sprint-10/Evidências/Gráfico_4.png)

* Quinto gráfico desenvolvido é um gráfico de barras verticais, das quais apresenta 10 nomes de diretores no eixo x e a quantidade de filmes produzidos por cada no eixo y. A pergunta que este gráfico busca responder é: Quais diretores mais produziram filmes?
![](/Sprint-10/Evidências/Gráfico_5.png)

* O sexto gráfico é um de dispersão em que tem como objetivo estabelecer a relação entre dois valores. A pergunta que este gráfico responde é a seguinte: 5-Relação entre orçamento e popularidade dos filmes;
![](/Sprint-10/Evidências/Gráfico_6.png)

* Sétimo gráfico é um gráfico de linhas, são comparados dois valores direfentes, são eles o orçamento e a bilheteria no eixo y e o titulo dos filmes no eixo x. A questão respondida é: Quais filmes com baixo orçamento tiveram grande sucesso de bilheteria?
![](/Sprint-10/Evidências/Gráfico_7.png)

* Oitavo gráfico é um de linhas com o objetivo de apresentar a oscilação de um valor durante os anos de 1960 a 2022. A questão respondida é: 4-Qual a quantidade de filmes lançados dos generos drama e romance ao longo dos anos?
![](/Sprint-10/Evidências/Gráfico_8.png)

* Indicadores KPIs: tenho 4 indicadores KPIs no início do dashboard, que apresentam as seguintes questões: orçamento médio dos filmes, bilheteria média dos filmes, duração média dos filmes e a popularidade média.
![](/Sprint-10/Evidências/Gráfico_KPI.png)

Após a construção de todos os gráficos, eu inseri uma imagem no início do dashboard que vai auxíliar no entendimento geral da analise.

#### Visão geral do dashboard no Quicksight
![](/Sprint-10/Evidências/Visão_Quicksight.png)

### Resultado final
Após todas as etapas do desafio final ter sido concluídas, o resultado é este dashboard desenvolvido usando os serviços da AWS e afins.

* [Acessar o dashboard PDF](https://github.com/LuanAlcolea/PB-Luan-Alcolea/blob/main/Sprint-10/Desafio/Dashboard_final_Luan_Alcolea.pdf)
![](/Sprint-10/Evidências/Dashboard_img.png)