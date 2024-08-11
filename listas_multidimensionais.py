
""" LISTAS UNIDIMENTIONAIS """

lista_unidimencional = [1, 2, 3]

""" LISTAS BIDIMENCIONAIS -> MATRIZ """

lista_bidimencional = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

lista1 = lista_bidimencional[0]
lista2 = lista_bidimencional[1]
lista3 = lista_bidimencional[2]
print(lista_bidimencional)
print(lista1)
print(lista2)
print(lista3)

print(lista_bidimencional[0][2]) # acessando elemento 2 da lista 1 dentro de uma lista multidimencional

# Matriz simétrica (Que quando substituir linha por columa os valores ficaram na exata mesma ordem)
matriz = [
    [1,2,3],
    [2,4,5],
    [3,5,2]
]

def simetrica(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    for i in range(linhas):
        for j in range(colunas): 
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

print(simetrica(matriz))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    