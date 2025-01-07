## Exercício Athena
### Preparar o bucket
Para iniciar o exercício devemos preparar o bucket. Criei um bucket chamado "exercicio-athena-luan" e baixei e carreguei o arquivo "nomes.csv" para dentro do bucket. Criei a pasta "queries" para guardar os resultados das analises dentro do Athena.
![Preparando-Arquivos](../Exercícios/Exercício-AWS-Athena/Preparando-Arquivos.png)
![](../Exercícios/Exercício-AWS-Athena/)
### Configuar o caminho para os resultados das queries
Configurei o caminho dos resultados das queries.
![Gerenciando-Configurações](../Exercícios/Exercício-AWS-Athena/Gerenciando-Configurações.png)
![](../Exercícios/Exercício-AWS-Athena/)
### Criando o banco de dados
Criei o banco de dados
![Criando-banco-de-dados](../Exercícios/Exercício-AWS-Athena/Criar-Banco-de-dados.png)
### Criando as tabelas
Criei as tabelas conforme o arquivo "nomes.csv"
![Criando-tabela](../Exercícios/Exercício-AWS-Athena/Criando-Tabela.png)
### Executando a querie final
Após executar a querie de teste, criei a querie requisitada e executei
![Resultado-Final](../Exercícios/Exercício-AWS-Athena/Resultado-Athena.png)

### Código da querie
```sql
with nomes as (
  select
    nome,
    floor(ano / 10) * 10 as decada,
    count(*) as contagem,
    row_number() over (partition by floor(ano / 10) * 10 order by count(*) desc) as ranking
  from meubanco
  where ano >= 1950
  group by nome, floor(ano / 10) * 10
)
select nome, decada
from nomes
where ranking <= 3
order by decada, ranking;
```
## Exercício Lambda
Neste exercício devemos criar uma função lambda que vai executar uma operação usando a biblitoteca pandas, devemos configurar um layer para que a função lambda consiga utilizar a biblioteca.
### Criando a função lambda
![Criando-Lambda](../Exercícios/Exercício-AWS-Lambda/Criando-Lambda.png)
### Construindo o código
![](../Exercícios/Exercício-AWS-Lambda/Primeira-Execução.png)
### Criando Layer
Preparando imagem docker
![](../Exercícios/Exercício-AWS-Lambda/Criando-Layer.png)
Código .py para carregar os arquivos no S3
![](../Exercícios/Exercício-AWS-Lambda/Criando-Layer-Codigo.png)
Configurando a camada no AWS Lambda
![](../Exercícios/Exercício-AWS-Lambda/Criando-Layer-3.png)
Execução final do exercício Lambda
![](../Exercícios/Exercício-AWS-Lambda/Resultado-Lambda.png)