# Para executar os scripts copie e cole em um arquivo python vazio.
# Este arquivo serve apenas para armazenar os scripts desenvolvidos no exercícios da Udemy
E01:
nome = "Teste"
idade = 24
ano_atual = 2024
ano_nascimento = ano_atual - idade
ano_idade_cem = ano_nascimento + 100

print(ano_idade_cem)

E02:
numeros = []

for i in range(3):
    numeros.append(i+1)
    if(numeros[i] % 2 == 0):
        print("Par: %d"%numeros[i])
    else: 
        print("Ímpar: %d"%numeros[i])

E03:
numeros = []
quantidade_numero = 20

for i in range(quantidade_numero + 1):
    numeros.append(i)
    if(numeros[i] % 2 == 0):
        print(numeros[i])

E04:
def verificar_primo(numero):
    if numero < 0: return False
    
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True

for i in range(2, 101):
    if verificar_primo(i):
        print(i)

E05:
dia = 22
mes = 10
ano = 2022

print("%d/%d/%d"%(dia,mes,ano))

E06:
a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

set_a = set(a)
set_b = set(b)

list_intersected = set_a & set_b

print(sorted(list_intersected))

E07:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numeros_impares = [num for num in a if num % 2 != 0]

print(numeros_impares)

E08:
palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']


def verificar_palindromo(palavra):
    # converter para low case e remover espaços
    palavra = palavra.replace(" ", "").lower()
    # retornar a palavra ao contrario
    return palavra == palavra[::-1]


for i in palavras:
    if verificar_palindromo(i):
        print(f"A palavra: {i} é um palíndromo")
    else:
        print(f"A palavra: {i} não é um palíndromo")

E09:
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice, (primeiroNome, sobreNome, idade) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(f"{indice} - {primeiroNome} {sobreNome} está com {idade} anos")

E10:
listaNormal = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']


def removerItensDuplicadosLista(lista):
    return list(set(lista))
    
print(removerItensDuplicadosLista(listaNormal))

E11:
import json

with open('person.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)

E12:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def potencia(value):
    return value * value


def my_map(list, f):
    nova_lista = []
    for i in list:
        nova_lista.append(f(i))
    return nova_lista


minha_lista = my_map(lista, potencia)
print(minha_lista)


E13:
with open('arquivo_texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    
print(conteudo, end='')

E14:
def imprimir_parametros(*args, **kwargs):
    for i in args:
        print(i)
        
    for j, k in kwargs.items():
        print(k)

imprimir_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

E15:
class Lampada:
    def __init__(self, estaLigada):
        self.ligada = estaLigada
    
    
    def liga(self):
        self.ligada = True
    
    
    def desliga(self):
        self.ligada = False
    
    
    def esta_ligada(self):
        return self.ligada
        

lampada = Lampada(False)
lampada.liga()
print(lampada.esta_ligada())
lampada.desliga()
print(lampada.esta_ligada())

E16:
string_com_valores = "1,3,4,6,10,76"


def somar_string(string):
    valores = string.split(",")
    valores = [int(valor) for valor in valores]

    return sum(valores)
    
print(somar_string(string_com_valores))

E17:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def dividir_lista(lista):
    tamanho = len(lista)
    tamanho_sub = tamanho // 3
    
    lista1 = lista[:tamanho_sub]
    lista2 = lista[tamanho_sub:tamanho_sub*2]
    lista3 = lista[tamanho_sub*2:]
    
    return lista1, lista2, lista3


lista1, lista2, lista3 = dividir_lista(lista)
print(lista1, lista2, lista3)

E18:
speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

valores_unicos = list(set(speed.values()))

print(valores_unicos)

E19:
import random

random_list = random.sample(range(500), 50)


mediana = 0
media = sum(random_list) / len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

lista_sorted = sorted(random_list)

if len(lista_sorted) % 2 == 1:
    mediana = lista_sorted[len(lista_sorted) // 2]
else:
    mid = len(lista_sorted) // 2
    mediana = (lista_sorted[mid - 1] + lista_sorted[mid]) / 2
    
print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")

E20:
a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = a[::-1]

print(b)

E21:
class Passaro:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som
        self.estado_voo = "Voando..."
        
    def voar(self):
        print(self.nome)
        print(self.estado_voo)
        
    def emitir_som(self):
        print(f"{self.nome} emitindo som: {self.som}")
        
class Pato(Passaro):
    def __init__(self, nome, som):
        super().__init__(nome, som)
    
    def voar(self):
        super().voar()
        
    def emitir_som(self):
        super().emitir_som()
    
class Pardal(Passaro):
    def __init__(self, nome, som):
        super().__init__(nome, som)
    
    def voar(self):
        super().voar()
        
    def emitir_som(self):
        super().emitir_som()

pato = Pato("Pato", "Quack Quack")
pardal = Pardal("Pardal", "Piu Piu")

pato.voar()
pato.emitir_som()
pardal.voar()
pardal.emitir_som()

E22:
class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = ''
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
pessoa = Pessoa(0)

pessoa.nome = "Nome"

print(pessoa.nome)

E23:
class Calculo:
    def __init__(self):
        pass
    
    def soma(self, x, y):
        return x + y
        
    
    def subtracao(self, x, y):
        return x - y
        

calculo = Calculo()
print("Somando: 4+5 = {calculo.soma(4, 5)}")
print("Subtraindo: 4-5 = {calculo.subtracao(4, 5)}")

E24:
class Ordenadora:
    def __init__(self, lista):
        self.listaBaguncada = lista

    
    def ordenacaoCrescente(self):
        self.listaBaguncada.sort()
        return self.listaBaguncada
    
    def ordenacaoDecrescente(self):
        self.listaBaguncada.sort(reverse=True)
        return self.listaBaguncada
        

listaCrescente = [3,4,2,1,5]
listaDecrescente = [9,7,6,8]

crescente = Ordenadora(listaCrescente)
decrecente = Ordenadora(listaDecrescente)

print(crescente.ordenacaoCrescente())
print(decrecente.ordenacaoDecrescente())

E25:
class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade, cor):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = cor
        
    
    def imprimir_valores(self):
        print(f"O avião de modelo {self.modelo} possui uma velocidade máxima de {self.velocidade_maxima}, capacidade para {self.capacidade} passageiros e é da cor {self.cor}")
        

aviao1 = Aviao("BOIENG456", "1500 km/h", 400, "Azul")
aviao2 = Aviao("Embraer Praetor 600", "863km/h", 14, "Azul")
aviao3 = Aviao("Antonov An-2", "258 Km/h", 12, "Azul")

aviao1.imprimir_valores()
aviao2.imprimir_valores()
aviao3.imprimir_valores()