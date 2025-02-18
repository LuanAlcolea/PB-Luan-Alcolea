# Desafio Sprint 9
## Resumo
Nesta etapa vamos processar os dados da camada Trusted e move-las corretamente para a camada Refined, um script que vai realizar essa etapa deve ser executado no AWS Glue. Os dados devem ser filtrados conforme a construção da modelagem multidimensional dos dados.

## Planejamento
O meu objetivo é preparar os dados para a construção do meu dashboard, que terá como objetivo analisar dados sobre atores, produtores e filmes, e suas diversas relações envolvendo multiplos dados. Contudo eu preciso organizar os dados presentes no data lake para que haja dados o suficiente para as futuras analises, por este motivo eu realize reingestão dos dados.

## Criação da modelagem de dados
Eu desenhei a modelagem de dados usando a ferramenta "draw.io" no navegador. Abaixo segue a imagem da modelagem multidimensional desenvolvida.
![](/Sprint-9/Evidências/Modelo_Multidimensional.png)

### Explicação da construção do modelo
* A tabela fato contém o primary key, id de data, id do filme e outros dados, como receita, orçamento e nota pública.
* A tabela dimensional data contém o id de data para relacionar com a fato através da relação de 1:1.
* A tabela ponte se conecta ao id do filme e estabelece uma relação de 1 para muitos na modelagem.
* A tabela dimensional filmes contém detalhes sobre o filme.
* A tabela dimensional atores contém detalhes sobre os atores que participaram da obra.
* A tabela dimensional diretores contém detalhes sobre os diretores que desenvolveram a obra.

## Reingestão de dados
Após a definição da modelagem de dados, eu decidi que eu preciso de mais dados para a construção do dashboard. Eu modifiquei o script de ingestão de dados para que ele busque mais dados da api tmdb e que reorganize os dados no json.

* [Ir para o script da reingestão de dados](https://github.com/LuanAlcolea/PB-Luan-Alcolea/tree/main/Sprint-9/Desafio/Extração_de_dados_tmdb.py)

![](/Sprint-9/Evidências/ev_reingestão_resultado.png)
![](/Sprint-9/Evidências/ev_reingestao_s3.png)

## Conversão dos dados
Com os dados corretamente extraídos da api para a camada raw, é hora de converter os dados para o formato parquet. Para isso eu modifiquei o script para que ele detecte os arquivos e converta para parquet corretamente.

* [Ir para o script da conversão de dados](https://github.com/LuanAlcolea/PB-Luan-Alcolea/tree/main/Sprint-9/Desafio/Processamento_raw_para_trusted.py)

![](/Sprint-9/Evidências/ev_conversão_resultado.png)
![](/Sprint-9/Evidências/ev_conversão_s3.png)

## Desenvolvimento do script
Neste ponto os dados no data lake estão prontos para serem filtrados e movidos para a camada refined. Criei o script no AWS Glue para criar as tabelas e armazenar de forma particionada dentro do S3.

* [Ir para o script do desafio](https://github.com/LuanAlcolea/PB-Luan-Alcolea/tree/main/Sprint-9/Desafio/Desafio-Sprint-9.py)

### Explicação do script
### Configurações de variáveis auxiliares
* Declarei três variáveis globais que irão auxiliar em acessar os dados dentro do data lake.
![](/Sprint-9/Evidências/ev_script_1.png)

### Criação de tabelas: tabela fato e a dimensão data
* Usando o PySpark eu crio a tabela fato selecionando dados do parquet de origem da api tmdb (json). Após, eu crio a tabela dimensão data e extraío os dados também dos dados da mesma origem.
![](/Sprint-9/Evidências/ev_script_2.png)

### Criação de tabelas: dimensão filme, dimensão atores e dimensão diretores
* Em seguida eu criei a tabela dimensão filme em que guarda detalhes dos filmes, as origens dos dados é de origem local (csv). Na ordem tem as tabelas dimensionais atores e diretores, aqui eu utilizo variáveis auxíliares para a criação correta dessas tabelas, pois cada select no pyspark pode haver apenas um explode.
![](/Sprint-9/Evidências/ev_script_3.png)

### Criação de tabelas: dimensão ponte
* Para ligar a tabela fato com varios IDs de atores e diretores, eu crio uma tabela ponte para estabelecer a relação de um para muitos na modelagem.
![](/Sprint-9/Evidências/ev_script_4.png)

### Salvar novas tabelas na camada refined
* Após todas as tabelas criadas no script, eu salvo todas na camada refined, cada um em sua pasta respectiva. Por fim, é aqui em que o script encerra.
![](/Sprint-9/Evidências/ev_script_5.png)

## Resultados de execução
Após todas as execuções os dados presentes na camada refined estão prontos para serem consultados. Criei o Crawler para visualizar as tabelas corretamente, criei um database para o crawler armazenar as tabelas, que eu chame de "data_lake_db", segue abaixo os resultados das consultas.
* O resultado da execução no AWS S3:
![](/Sprint-9/Evidências/ev_refined.png)

* Resultado da criação das tabelas no glue
![](/Sprint-9/Evidências/ev_tabelas.png)
* Resultado da consulta padrão feita na tabela fato
![](/Sprint-9/Evidências/ev_tabela_fato.png)
* Resultado da consulta padrão feita na dimensão data
![](/Sprint-9/Evidências/ev_tabela_data.png)
* Resultado da consulta padrão feita na dimensão ponte
![](/Sprint-9/Evidências/ev_tabela_ponte.png)

Esta então é a entrega da etapa 4 do desafio final, neste momento os dados se encontrar prontos para serem utilizados na criação do dashboard, que representa a ultima etapa do desafio final.