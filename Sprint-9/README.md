# Resumo
O objetivo desta sprint é preparar o caminho final para a construção do dashboard, vamos planejar como os dados ficarão dispostos no banco de dados e quais são os dados que vamos utilizar. Primeiramente vamos criar a modelagem de dados multidimensional, através dessa modelagem vamos desenvolver um script que vai ler os dados da camada trusted e vai separa-los em tabelas correspondentes a modelagem para a camada refined. Neste ponto os dados estarão prontos para serem utilizados no dashboard. Esta etapa representa a quarta entrega do desafio final.

# Desafio proposto
### Resumo
Para começar o desafio eu realizei uma outra analise sobre como eu vou entregar o desafio final, então eu tomei a decisão de buscar mais dados da API TMDB para seguir corretamente a minha modelagem de dados. As minhas perguntas foram renovadas nesta sprint também.

* [Ir para o desafio](https://github.com/LuanAlcolea/PB-Luan-Alcolea/tree/main/Sprint-9/Desafio/README.md)

### Modelagem dos dados
Abaixo esta a imagem da minha modelagem de dados multidimensional
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

# Evidências de execução
Esta parte da documentação demonstra os resultados da execução dos scripts produzidos nesta sprint.

*  [Ir para as evidências](https://github.com/LuanAlcolea/PB-Luan-Alcolea/tree/main/Sprint-9/Evidências/README.md)

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