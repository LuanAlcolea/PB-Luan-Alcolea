# Desafio Sprint 3
## Resumo do desafio
Neste desafio devemos extrair e processar dados de um dataframe chamado "googleplaystore.csv" utilizando a linguagem Python na ferramenta Jupyter Notebook. Para a extração e processamento de dados é utilizado a biblioteca Pandas e para a geração de gráficos é utilizado o Matplotlib. O desafio foi separado em 8 etapas, cada uma com a comanda sobre o que fazer com o dataframe.

## Preparação do ambiente
Para iniciar o desafio devemos preparar o ambiente de desenvolvimento, isto é baixar e instalar a IDE Jupyter Notebook. Eu optei por utilizar a extensão do Jupyter no VSCode para desenvolver o desafio. Após a configuração devemos importar para o código as bibliotecas Pandas e Matplotlib.

## Desenvolvimento do desafio
Abaixo está todos os códigos utilizados para o desenvolvimento do desafio.
### Configurações prévias:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('googleplaystore.csv')

def get_coluna(coluna):
    return df[coluna].replace({',': '', '\+': ''}, regex=True)

# Converter para exibir numeros inteiros e não notação cientifica
pd.set_option('display.float_format', '{:,.0f}'.format)
```

### 1: Remover itens duplicados

```python
print(f"Quantidade de linhas originais: {df.shape[0]}")

df = df.drop_duplicates()

print(f"Quantidade de linhas sem duplicações: {df.shape[0]}")

```

### 2: Criar gráficos de barras contendo o top 5 apps mais instalados

```python
installs = get_coluna('Installs')

installs = pd.to_numeric(installs, errors='coerce')

five_installs = installs.nlargest(5)

five_apps = df.loc[five_installs.index, 'App']

plt.figure(figsize=(10, 6))
plt.bar(five_apps, five_installs, color='skyblue')

plt.title('Top 5 Apps por Instalações', fontsize=16)
plt.xlabel('Aplicativos', fontsize=12)
plt.ylabel('Número de Instalações', fontsize=12)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
```

### 3: Gráfico Pie Char mostrando as categorias de apps de acordo com sua frequência

```python
from collections import Counter

frequencias = Counter(get_coluna('Category'))
frequencias = pd.Series(frequencias)
frequencias = frequencias[frequencias.index != '1.9']
frequencias = frequencias.sort_values(ascending=False)

plt.figure(figsize=(9, 9))

outputs = plt.pie(frequencias, labels=frequencias.index, startangle=90,
                  textprops={'fontsize': 6}, labeldistance=1.1, rotatelabels=True)

if len(outputs) == 3:
    wedges, texts, autotexts = outputs
else:
    wedges, texts = outputs

plt.show()
```

### 4: Imprimir qual app mais caro no dataset
```python
coluna_price = df['Price'] = df['Price'].replace({'\$': '', ',': ''}, regex=True)
coluna_price = pd.to_numeric(df['Price'], errors='coerce')
coluna_app = get_coluna('App')

indice_max = coluna_price.idxmax()

app_mais_caro = df.loc[indice_max, 'App']
valor_maximo = coluna_price[indice_max]

print(f"App mais caro: {app_mais_caro} - {valor_maximo}")
```

### 5: Imprimir quantos apps são classificados como "Mature 17+"
```python
mature = get_coluna('Content Rating')

mature_apps = df[df['Content Rating'] == 'Mature 17+']['App']

quantidade = len(mature_apps)

print(f"São {quantidade} apps que são classificados como 'Mature 17+'")
```

### 6: Imprimir o top 10 apps de acordo com o número de reviews e o respectivo número de reviews
```python
reviews = pd.to_numeric(df['Reviews'], errors='coerce')

apps = df.loc[df['App'].duplicated(keep='first') == False, ['App', 'Reviews']]

apps['Reviews'] = reviews

apps = apps.sort_values(by='Reviews', ascending=False).head(10)

print(apps)
```

### 7: Criar dois calculos usando o dataset
```python
# top 10 generos de app menos utilizados
top_five_genres = df['Genres'].value_counts().tail(10)

print("Top 10 generos de apps menos usados:")
print(top_five_genres)

# App com o maior nome
apps = df['App']

app_com_maior_nome = apps.loc[apps.str.len().idxmax()]

print(f"O App com o maior nome é: {app_com_maior_nome}")
```

### 8: Criar dois gráficos utilizando o dataset
```python
plt.rc('font', size=8)

# Gráfico em barras laterais para mostrar os 10 generos de apps mais usados
coluna_genero = df['Category'].value_counts().head(10)
coluna_genero.plot.barh()
plt.xlabel('Número de Apps')
plt.ylabel('Categoria')
plt.title('Top 10 categorias de Apps')
plt.show()

# Quantidade de apps lançados para cada versão de android
coluna_androidver = df['Android Ver'].value_counts().sort_index()
coluna_androidver.plot.line(marker='o')
plt.xlabel('Versão do Android')
plt.ylabel('Número de Apps')
plt.title('Quantidade de Apps por versão do Android')
plt.xticks(rotation=45)
plt.show()
```