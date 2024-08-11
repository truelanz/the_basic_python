
""" ESTRUTURA DE REPETIÇÃO - FOR """

# TIPOS DE FOR:
# for <variavel/x/i> in <sequencia>
lista = [1, 2, 3]
for x in lista:
   print(x)
   
character = 'python'
for c in character:
    if c in 'yo':
        print(c)
   

# for <variavel/x/i> in range (start, stop, step)
for x in range(10):
    print(x, end=', ')

print()
for y in range(0, 20, 2):
    print(y, end=', ')

print()
lista2 = ['meu', 'ovo', 'esquerdo']
for i in range(len(lista2)):
    print(lista2[i], end=' | ')
    
# ACUMULADOR
print()
acumulator = 0
for x in range(0, 11):
    if x % 2 == 0:
        acumulator += x # SOMA DE TODOS OS NÚMEROS PARES
print(acumulator)

# RETORNE AS VOGAIS QUE OCORREM NA LISTA:
str_list = ['João', 'Roberto', 'Rafael'] # Caracteres com acentos não são considerados vogais e sim caracteres especiais.
for name in str_list:
    for c in name:
        if c in 'aeiou':
            print(c, end=', ')