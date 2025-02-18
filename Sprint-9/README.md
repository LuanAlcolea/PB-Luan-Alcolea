# Resumo
O objetivo desta sprint é preparar os dados que serão utilizados na construção do dashboard, vamos desenvolver um script que vai filtrar os dados do data lake e armazená-los de forma correta para futuras consultas. Esta sprint é uma oportunidade para aprimorar o planejamento da entrega final, desde as questões que serão utilizadas, até como elas serão dispostas no dashboard.
O primeiro passo do desafio é desenvolver a modelagem multidimensional dos dados que estarão presentes na camada refined, neste ponto as questões que serão respondidas no dashboard devem estar claras e bem elaboradas. Após a conclusão da modelagem dos dados vamos construir o script do desafio.

# Desafio proposto
* [Ir para o desafio](https://github.com/LuanAlcolea/PB-Luan-Alcolea/tree/main/Sprint-9/Desafio/README.md)
### Reingestão de mais dados da API TMDB
Para começar o desafio eu realizei uma outra analise sobre como eu vou entregar o desafio final, então eu tomei a decisão de buscar mais dados da API TMDB para seguir corretamente a minha modelagem de dados. Eu decidi renovar as minhas perguntas para o dashboard final, eu optei por tratar de questões que envolvam filmes, atores/atrizes e diretores.

### Modelagem dos dados
* Abaixo esta a imagem da minha modelagem de dados multidimensional
![](/Sprint-9/Evidências/Modelo_Multidimensional.png)

### Questões preparadas
As minhas perguntas tem como objetivo extraír insights relevantes ao analisar dados de filmes, atores/atrizes e produtores.
```
1-Quais filmes com baixo orçamento tiveram grande sucesso de bilheteria?
2-Qual foi o genero entre drama e romance que mais foram produzidos entre os anos?
3-Qual é a quantidade de filmes produzidos por diretores mulheres em comparação com filmes produzidos por diretores homens?
4-Quais atores mais interpretaram o mesmo personagem em diferentes filmes?
5-Quais atores mais contracenaram juntos ao longo dos anos?
6-Qual é a quantidade de diretores que produziram filmes juntos?
7-Quais diretores mais produziram filmes?
8-Quais diretores atuaram como atores nos filmes.
```
### A construção do script do desafio
Após as reingestões e processamento de dados eu escrevi o script para trazer os dados da camada trusted para a camada refined, o script extrai os dados para a construção das tabelas necessárias de dados de origem local, que representa os arquivos no formato "csv", e de origem da API TMDB, que representa o formato "json".
O script desenvolvido no AWS Glue acessa os dados que estão presentes na camada trusted e utilizando o PyPSark vai filtrar e realizar junções de dados para a criação de tabelas de dados, essas tabelas são armazenadas na camada refined. A camada refined contém os dados filtrados, confiáveis e prontos para serem utilizados.

# Evidências de execução
*  [Ir para as evidências](https://github.com/LuanAlcolea/PB-Luan-Alcolea/tree/main/Sprint-9/Evidências/README.md)

Esta parte da documentação demonstra os resultados da execução dos scripts produzidos nesta sprint.

* Imagem do AWS S3 após a reingestão dos dados
![](/Sprint-9/Evidências/ev_reingestao_s3.png)
* Imagem do AWS S3 após as conversões
![](/Sprint-9/Evidências/ev_conversão_s3.png)
* Imagem da camada refined após a execução do script
![](/Sprint-9/Evidências/ev_refined.png)
* Imagem da consulta da tabela fato após a criação do Crawler
![](/Sprint-9/Evidências/ev_tabela_fato.png)

# Conclusão
Esta sprint representa uma etapa muito importante para o desafio final, após a execução dos passos desta etapa estamos aptos a utilizar os dados no dashboard. Não houve exercícios e cursos exernos a serem realizados.