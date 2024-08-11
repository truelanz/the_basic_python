
""" STRINGS """

nome = 'Alan '
sobrenome = 'Resende'
espacoEmBranco = '     t   e ste '

# Concatenação de Strings
print (nome + sobrenome)

# Multiplicando string (número inteiro)
print (nome * 4)

# Ver se o valor de uma variável está contida dentro de outra
letra = 'la'
print (letra in nome) #TRUE

# Verificar se valor exato da variável 
print (letra is str('la')) #TRUE

# Retornar tamanho da string
print (len(sobrenome))

# Indexação de String
print (sobrenome[3])

# Acessar indice da string de trás para frente
# 0 | 1 | 2 | 3 | 4 | 5 | 6
#-7 |-6 |-5 |-4 |-3 |-2 | 7
# R | E | S | E | N | D | E
print (sobrenome[-3])

#Acessar parte de uma string por indexação
print (sobrenome[1:4]) # [começo:final] indice 'final' não é inclusivo
print (sobrenome[:6]) # quando não indica nenhum número no 'começo' ele começa desde o zero
print (sobrenome[3:]) # quando não indica nenhum número no 'final' ele vai até o fim


""" MÉTODOS PARA TRABALHAR COM STRINGS """

# Procurar indice de um caractere em uma string
print (sobrenome.find('s'))
# Retornar a frequência de um caractere em uma string
print (sobrenome.count('e'))
# Substituir um caractere por outro
print (sobrenome.replace('e', 'x'))
print (sobrenome.replace('x', 'e'))
# Tornar primeiro caractere Maiúsculo
print (sobrenome.capitalize())
# Tornar todos os caracteres Maiúsculos
print (sobrenome.upper())
# Tornar todos os caracteres minúsculos
print (sobrenome.lower())
# Remover espaços em branco
print (espacoEmBranco.strip())
print (espacoEmBranco.replace(' ', ''))