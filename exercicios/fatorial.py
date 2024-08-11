""" Implementar uma função recursiva em Python
para calcular o fatorial de um número inteiro
positivo passado como parâmetro. """

import time

# FUNÇÃO ITERATIVA
def fatorial(num): # O número digitado pelo usuário, 3 por exemplo
    result = 1 # para a multiplicação começar do 1.
    for i in range(1, num + 1): # do 1 até o número digitado pelo usuário. 1 até o 3
        result *= i # 1*1=1, 2*1=2, 2*2=4, 3*2=6
    return result

# FUNÇÃO RECURSIVA
def fat(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fat(n - 1) 

start = time.time()
fatorial(1500) 
print('Função Iterativa: {} segundos'.format(time.time() - start))

start = time.time()
fat(900)
print('Função Recursiva: {} segundos'.format(time.time() - start))