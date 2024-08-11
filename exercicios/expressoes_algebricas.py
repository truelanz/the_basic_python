""" 
Escreva expressões algébricas Python correspondentes aos seguintes comandos:  
 
1. A soma dos 5 primeiros inteiros positivos.
2. A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
3. O número de vezes que 73 cabe em 403.
4. O resto de quando 403 é dividido por 73.
5. 2 à 10ª potência.
6. O valor absoluto da distância entre a altura de Sara (54 polegadas) e a
altura de Mark (57 polegadas).
7. O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50. 
"""

# 1)
soma = 0
for i in range(1, 6):
    soma += i

print ('A soma dos 5 primeiros números é igual a:', soma)

# 2)
saraAge = 23
markAge = 19
fatimaAge = 31

mediaAge = saraAge + markAge + fatimaAge / 3
print ('A média da idade de Sara, Mark e Fática é de:', round(mediaAge, 2), 'anos')

# 3)
n1 = 73
n2 = 403
result = 403 / 73

print ('O número', n1, 'cabe', round(result, 2), 'vezes dentro do número', n2)

# 4)
print ('O resto de', n2, 'quando dividido por', n1, 'é:', n2 % n1)

# 5)
print ('2 à potência de 10ª é:', 2 ** 10)

# 6)
saraHeight = 54
markHeight = 57
print ('O valor absoluto entre a altura de Sara e Mark é:', abs(saraHeight - markHeight))

precos = [34.99, 29.95, 31.50]
print ('O menor preço é', min(precos))

