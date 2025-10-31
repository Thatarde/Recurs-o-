"""
lista_numeros = array da lista dos números a serem procurados, exemplo: [1, 2, 3]
valor = valor a ser procurado no array
inicio = indice de inicio da lista, exemplo: lista_numeros[0] = 1
fim = índice do fim da lista, exemplo: lista_numeros[2] = 3
"""

# Inicio

def busca_binaria(lista_numeros, valor, inicio, fim): # Função da busca binária

    meio = (inicio + fim)//2 # Calculo da metade do índice total e arredondamento para ser inteiro

    # Verificação do caso base de falha, não estar presente na lista
    if meio < inicio or meio > fim:
        return "não presente na lista"

    if lista_numeros[meio] == valor: # Caso base, dar certo na primeira tentativa
        return meio
    elif lista_numeros[meio] > valor: # Procura no lado esquerdo da lista
        return busca_binaria(lista_numeros, valor, inicio, meio - 1) # Recursividade
    else: # Procura no lado direito da lista
        return busca_binaria(lista_numeros, valor, meio + 1, fim) # Recursividade



print("Digite zero para finalizar o programa")
print("-"*50)

lista_numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # Definindo o array

while True:
    valor = int(input("Digite o número a ser procurado: ")) # Pergunta de qual valor procurar

    if valor <= 0: # Possibilidade de finalizar o programa
        break

    # Chamada e print do resultado da função
    print(f'O índice do valor procurado é {busca_binaria(lista_numeros, valor, 0, len(lista_numeros) - 1)}')
    print("-"*50)

lista_numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # Definindo o array

# Fim