# Desafio
## Proposta do desafio
O usuário deve criar dois shell scripts que vai manipular e extrair informações de um arquivo chamado "dados_de_vendas.csv". As habilidades a serem treinadas são: ambientação do sistema operacional Linux e a lógica de programação utilizando a linguagem shell script.

## Script Processamento_de_Vendas.sh
O primeiro script chamado "processamento_de_vendas.sh" será o responsável por criar diretórios, copiar, compactar e extrair dados do arquivo .csv. As informações do arquivo deve ser registradas em um arquivo de texto chamado "relatório.txt", sua execução deve ocorrer quatro vezes de segunda-feira a sexta-feira as 15:27.

## Script Consolidador_Processamento_de_Vendas.sh
Este script deve mesclar os quatros relatórios gerados anteriormente em um só chamado "relatório-final.txt"

## Agendamento de execução
O agendamento das quatro execuções deve ser feita utilizando a ferramenta do Linux chamada "Cron"

## Tarefas manuais
A criação da pasta ecommerce, a atualização das informações de cada .csv e a execução do script "Consolidador_processamento_de_vendas.sh" deve ser feita manualmente.

## Passo a passo
Primeiramente eu criei o diretorio ecommerce, dentro dele desenvolvi o "processamento_de_vendas.sh" e o "consolidador_de_vendas.sh", para testar eu executei manualmente os scripts, quando eu percebi que estavam em ordem, realizei o agendamento da execução do script no crontab. Preparei mais 3 versões com dados atualizados do "dados_de_vendas.csv". No primeiro dia eu não consegui inicializar o serviço cron a tempo, então a primeira execução ocorreu as 15:27, entretanto as execuções seguidas ocorreu no tempo e dias esperados. Para desenvolver o shell script eu procurei na internet sobre como implementar diversas funcionalidades, pois essa é a minha primeira experiência com a criação de rotinas no shell script.
