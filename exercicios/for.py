""" Exercício 3. Cap. 5 Ex 1c

Desenvolver os diagramas de blocos e as codificações em português estruturado usando
laço incondicional (para) do seguinte problema: Construir um programa que apresente a
soma dos cem primeiros números naturais (1 + 2 + 3 +...+ 98 + 99 + 100). """

soma = 0

for i in range(1, 101):
    soma += i

print("A soma dos 100 primeiros números Naturais é:", soma)