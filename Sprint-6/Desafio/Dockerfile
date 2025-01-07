# Usar imagem base do python
FROM python:3.11.9
# Definir diretorio de trabalho do container
WORKDIR /app 
# Copia os arquivos do diretorio atual para dentro do diretorio do container
COPY . . 
# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt
# Definir o volume
VOLUME /app/data
# Executar script
CMD ["python", "Script.py"]
