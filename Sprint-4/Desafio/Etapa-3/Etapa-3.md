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