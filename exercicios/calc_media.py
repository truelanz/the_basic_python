""" Exercício 2. Cap. 4 Ex 3c

Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno
representadas pelas variáveis N1, N2, N3 e N4. Calcular a média aritmética
(variável MD) desse aluno e apresentar a mensagem “Aluno Aprovado com média” se a
média obtida for maior ou igual a 5; caso contrário, apresentar a mensagem “Aluno
Reprovado com média”. Informar também, após a apresentação das mensagens, o valor
da média obtida pelo aluno. """

n1 = float(input("Digite sua nota: "))
n2 = float(input("Digite sua nota: "))
n3 = float(input("Digite sua nota: "))
n4 = float(input("Digite sua nota: "))

media = (n1 + n2 + n3 + n4) / 4

if media < 5:
    print ("Você foi reprovado", media)
else:
    print ("Você foi aprovado com a nota:", media)