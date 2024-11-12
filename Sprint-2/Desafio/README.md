# Desafio
## Proposta do desafio
Para praticarmos os conhecimentos em SQL, foi proposto o desafio de normalizar e dimensionar uma tabela chamada tb_locacao, do arquivo concencionária.sql. O processo de normalização refere-se a ação de separar em diversas tabelas os conteúdos que estão em uma única tabela. Após esse processo obtemos a versão relacional dela, da qual é útil para inserção, modificação e deleção de dados. Com a versão relacional devemos converter para a dimensional, eu optei pelo formato snow flake, essa versão das tabelas é útil para consultas de dados.

## Concensionária.sql
Este arquivo contém a tabela tb_locacao da qual contém dados de locação de carros, dados de clientes, vendedores, datas e outras informaçoes dos veículos.

## Passo a passo
## Processo de normalização
Devemos importar o arquivo concessionária.sql para dentro do programa de banco de dados, nela vai conter a tabela tb_locacao. Eu então analisei os dados contidos e criei tabelas novas, conectando elas através de IDs únicos, o resultado foi novas tabelas relacionais prontas para serem convertidas para o modelo dimensional.

## Processo de conversão relacional para dimensional
Utilizando o resultado da normalização eu criei as tabelas dimensionais, usando os mesmo nomes da tabela relacional porem com as letras "dim_" no começo de seu nome. A tabela fato é chamada de fato_locacao, é o responsável por conectar com as outras tabelas, no formato snow flake.

## Anotações
Primeiramente eu estudei sobre o conteúdo, assisti o vídeo proposto e comecei a implementação, realizei a normalização sem grandes dificuldades, entretanto o dimensionamento eu escrevi utilizando o "CREATE TABLE" ao ínves do "CREATE VIEW" proposto no vídeo, pois o último não se conecta as outras tabelas no modo diagrama

## Arquivos fornecidos

* Concessionaria.sql.