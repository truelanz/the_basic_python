""" Dada a lista de notas de trabalho de casa dos alunos
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

escreva:
Uma expressão que avalia para o número de 7 notas.
Uma instrução que muda a última nota para 4.
Uma expressão que avalia para a nota mais alta.
Uma instrução que classifica as notas da lista.
Uma expressão que avalia para a média das notas. """

# Uma instrução que muda a última nota para 4.
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
notas[-1] = 4

print(notas)

# Uma expressão que avalia para a nota mais alta.
print(max(notas))

# Uma instrução que classifica as notas da lista.
print(sorted(notas))
print(sorted(notas, reverse=True))

# Uma expressão que avalia para a média das notas.s
i = 0
soma = 0
for i in range (len(notas)):
    soma += notas[i]

media = soma / (i+1)
print(media)

