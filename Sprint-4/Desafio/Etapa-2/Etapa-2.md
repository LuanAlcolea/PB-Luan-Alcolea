# Etapa 2: É possível reutilizar containers?

### Sim, é possível reutilizar! Devemos localizar o nome ou id do container, após isso executar o comando para reiniciar e conectar o container parado no terminal, entretanto para usar o comando "attach" o container deve estar em execução.

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