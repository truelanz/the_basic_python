
"""  OPERADORES RELACIONAIS """
# == (é igual?)
# != (é diferente?)
# < (menor que) > (maior que) <= (menor ou igual) >= (maior ou igual)

# As expressões aritmetícas tem precedência sobre as lógicas. Ex:
print (2 + 1 >= 3)


""" OPERADORES LÓGICOS """
# 1º - not (negação parecido com != (se a expressão for falsa (false)))
# 2º - or (ou, se alguma das expressões for verdadeira (true))
# 3º - and (e, && (todas as expressões devem ser verdadeiras))
print (3 > 1 and 5 == 5 and 6 < 8) #TRUE
print (not 1 > 3 and 5 == 5 and 6 < 8) #TRUE
print (not 1 > 3 or 5 == 5 and 50 < 8) #TRUE

# in/not in (pertence/não pertence)
print (4 in [5, 10, 44]) #FALSE
print (4 not in [5, 10, 44]) #TRUE

# is/is not (é/não é)
print (1 is 2) #FALSE
print (1 is not 2) #TRUE
print (5.0 is 5) #FALSE - o tipo também conta.

"""  PRECEDÊNCIA ENTRE OS OPERADORES """
# 1º ( )
# 2º **, *, /, -, +
# 3º == < > != >= <=
# 4º not, or, and, in/not in, is,is not