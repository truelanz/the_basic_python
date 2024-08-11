""" 
Dados três valores positivos, A, B e C, construiur um programa que verifica se os
mesmo podem ser os comprimentos dos lados de um triângulo.

Verificar e imprimir se o triângulo é:
EQUILÁTERO: Posui os 3 lados iguais
ISÓSCELES: Possui dois lados iguais
ESCALENO: Possui todos os lados diferentes.
"""

a = eval((input('Digite o valor A: ')))
b = eval((input('Digite o valor B: ')))
c = eval((input('Digite o valor C: ')))

biggestSide = max(a, b, c)

if biggestSide < a + b + c - biggestSide:
    print('Os lados formam um triângulo!')
    if a == b == c:
        print('triângulo equilátero')
    elif (a != b)  and (a != c) and (b != c):
        print('triângulo escaleno')
    else:
        print('triângulo isósceles')
else:
    print('Os lados não formam um triângulo')



