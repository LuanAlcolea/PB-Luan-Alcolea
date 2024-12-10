# Desafio Sprint 4
## Resumo do desafio
Neste desafio devemos configurar a ferramenta docker para executar scripts Python. Para isso devemos criar uma imagem que vai preparar o ambiente de desenvolvimento do Python, a partir desta imagem devemos instanciar o container que vai executar um script Python, na ultima etapa devemos criar um script que mascara uma palavra usando o SHA-1.
## Desenvolvimento do desafio
Eu realizei o desafio na IDE VSCode e usei o docker no terminal da IDE. O desafio é separado em 3 etapas, e cada uma com uma comanda específica.
## Etapa 1: Criar uma imagem e iniciar um container para executar um scripts python

### 1. Montar a imagem
```
docker build -t carguru .
```
### 2. Iniciar container no modo interativo
```
docker run -it carguru
```

# Etapa 2: É possível reutilizar containers?

Sim, é possível reutilizar! Devemos localizar o nome ou id do container, após isso executar o comando para reiniciar e conectar o container parado no terminal, entretanto para usar o comando "attach" o container deve estar em execução.

### 1. Localizar o container
```
docker ps -a
```
### 2. Reinicia o container
```
docker start "nome_id_container"
```
### 3. Conecta novamente ao terminal
```
docker attach "nome_id_container"
```

# Etapa 3: Algoritmo para mascarar palavras com o SHA-1

## Parte 1: criação do script
```
1. Receber input do usuário
2. Gerar hash da string usando o sha-1
3. Imprimir a palavra usando o hexdigest
4. Retornar a etapa 1
```

## Parte 2: Criar uma imagem docker chamada "mascarar-dados" que execute o script

```
docker build -t mascarar-dados
```

## Parte 3: Iniciar um container a partir da imagem
```
docker run -it mascarar-dados
```
Nota: na orientação da parte 3 é dito que o container deve ser inicializado enviando palavras para o mascaramento, eu optei por usar o input do usuário para deixar o script interativo. Entretanto se for necessário iniciar o container e enviar argumentos diretamente pelo terminal, devemos utilizar no dockerfile a palavra chave ENTRYPOINT no lugar do CMD. O comando de inicialização com argumentos diretos é deste modo:
```
docker run -it mascarar-dados parametro1 parametro2 parametro3
```
## Parte 4: Registrar conteúdo desenvolvidos
Nesta etapa eu registrei aqui no github os conteúdos desenvolvidos.