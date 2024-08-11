""""" DATA TYPES """""

# nt, float, bool, str, list, tuple.

# Cada dado é armazenado na memóra na forma de objetos.
# e todo objeto possui um TIPO e um VALOR

print(type(3))
print(type('Eii'))

# Variáves em Python não possuem  um tipo (como C e JAVA por exemplo). 
# Elas apenas apontam temporariamente par aum obj na memória.

inteito = int(10) # A função int() e float() por exemplo, são chamadas de "construtor"

# Conversão inplícita: bool < int < float, ex:
print(True + 1, False + 1, 5 + 5.00)

# Conversão explícita:
n1 = 5.67
print(int(n1))



