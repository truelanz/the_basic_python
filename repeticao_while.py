""" ESTRUTURA DE REPETIÇÃO - WHILE """

i = 90
while i < 100: # Enquanto a condição for verdadeira
    print(i, end=', ') # Executar essa instrução
    i += 1 

print()

x = 90
while x != 100: # Enquanto a condição for Falsa
    print(x, end=', ') # Executar essa instrução
    x += 1
    
    
print()
    
# Fatorial
# [1*2*3*4*5]
# somar de modo iterativo o número atual ao número anterior
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1) # fatoria(n-1)
    
print(fatorial(5))

print()

# Digite um número até que ele seja positivo:
user_input = eval(input('Digite um número:'))
while user_input < 0:
    user_input = eval(input('O número deve ser positivo: '))
    
print(user_input)

    
# Armazenar elementos em um lista com WHILE
list_names = []
input_list = input("Digite um nome: ")
while input_list != '':
    list_names.append(input_list)
    input_list = input("Digite um nome: ")

print(list_names)