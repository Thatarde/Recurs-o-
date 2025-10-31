def fatorial(n): # Definição da função
  if n == 0 or n == 1: # Definição do caso base para a chamada não ser infinita
    return 1 # 0 e 1 fatoriais são iguais a 1

  else: # Caso o valor não seja 0 ou 1
    fat = n * fatorial(n-1) # Defini-se uma variável que fará o número do fatorial vezes a chamada dela mesma menos 1 até ser igual à 1
  """
  Lógica do calculo:

  fatorial(4) = 4 * fatorial(3) <- igual à 4 * fatorial(4 - 1)
  fatorial(3) = 3 * fatorial(2)
  fatorial(2) = 2 * fatorial(1)
  fatorial(1) = 1

  fatorial(1) = 1 * 1 = 1
  fatorial(2) = 2 * 1 = 2
  fatorial(3) = 3 * 2 = 6
  fatorial(4) = 4 * 6 = 24
  """
  return fat # Após todo o calculo multiplicação de trás para frente, retorna o valor do fatorial

print(fatorial(4)) # Fatorial a ser calculado (input)

