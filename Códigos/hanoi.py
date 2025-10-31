def hanoi(n, origem, destino):
    if n == 1:
        print(f"Mover disco 1 de {pino_para_nome(origem)} para {pino_para_nome(destino)}")
    else:
        auxiliar = 6 - (origem + destino)
        hanoi(n - 1, origem, auxiliar)
        print(f"Mover disco {n} de {pino_para_nome(origem)} para {pino_para_nome(destino)}")
        hanoi(n - 1, auxiliar, destino)

def pino_para_nome(numero):
    #Converte número do pino para nome (A, B, C)
    return ["A", "B", "C"][numero-1]

print("=== RESOLUÇÃO TORRES DE HANÔI ===")
hanoi(3, 1, 3)  # Move 3 discos do pino A para pino C