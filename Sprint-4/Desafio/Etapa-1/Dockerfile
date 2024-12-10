 # Usar imagem base do python
FROM python:3.10-slim
# Definir diretorio de trabalho do container
WORKDIR /app 
# Copia os arquivos do diretorio atual para dentro do diretorio do container
COPY . . 
# Executar o primeiro script python
CMD ["sh", "-c", "python $(ls *.py | head -n 1)"]
# Para executar o container com argumentos é necessário usar o ENTRYPOINT no lugar do CMD