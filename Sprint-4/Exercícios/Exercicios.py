# Arquivo de exercícios realizados na sprint
# E01:
def get_arquivo(nomearquivo):
    with open(nomearquivo, 'r') as arquivo:
        numeros = list(map(lambda linha: int(linha.strip()), arquivo))
        return numeros

arquivo = get_arquivo('number.txt')

# Extrair os 5 maiores numeros
pares = list(filter(lambda x: x % 2 == 0, arquivo))
cinco_maiores_pares = sorted(pares, reverse=True)[:5]
# Somar a lista dos 5 maiores numeros pares
soma = sum(cinco_maiores_pares)
# Imprimir resultados
print(cinco_maiores_pares)
print(soma)

#E02:
def conta_vogais(texto:str)-> int:
    vogais = 'AaEeIiOoUu'

    lista_vogais = list(filter(lambda letra: letra in vogais, texto))

    return len(lista_vogais)
#E03:
from functools import reduce

def calcula_saldo(lancamentos) -> float:
    #continue este código
    total = list(map(lambda valor: valor[0] if valor[1] == 'C' else -valor[0], lancamentos))
    total = reduce(lambda x, y: x + y, total, 0)
    return total
#E04:
def calcular_valor_maximo(operadores,operandos) -> float:
    valores = map(lambda op:
                  (op[0] == '+' and op[1][0] + op[1][1]) or
                  (op[0] == '-' and op[1][0] - op[1][1]) or
                  (op[0] == '*' and op[1][0] * op[1][1]) or
                  (op[0] == '/' and op[1][0] / op[1][1]) or
                  (op[0] == '%' and op[1][0] % op[1][1]),
                  zip(operadores, operandos))
    total = max(valores)
    return total
#E05:
def processar_dados(nomearquivo):
    with open(nomearquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        
        estudantes = []

        for linha in linhas:
            dados = linha.strip().split(',')

            nome = dados[0]
            notas = list(map(int, dados[1:]))

            maiores_notas = sorted(notas, reverse=True)[:3]

            media = round(sum(maiores_notas) / 3, 2)

            estudantes.append((nome, maiores_notas, media))

        estudantes = sorted(estudantes, key=lambda x: x[0])

        for estudante in estudantes:
            nome, maiores_notas, media = estudante
            print(f"Nome: {nome} Notas: {maiores_notas} Média: {media}")

processar_dados('estudantes.csv')
#E06:
def maiores_que_media(conteudo:dict)->list:
    return list(map(lambda item: (item[0], item[1]), sorted(filter(lambda x: x[1] >= sum(conteudo.values()) / len(conteudo), conteudo.items()), key=lambda x: x[1])))
#E07:
def pares_ate(n:int):
    for i in range(2, n+1, 2):
        yield i