
def b_b(lista, elemento, index_inicio, index_fim):
    
    meio = (index_inicio + index_fim) // 2
    
    if elemento == lista[meio]:
        return meio
    if elemento < lista[meio]:
        return b_b(lista, elemento, index_inicio, meio - 1)
    if elemento > lista[meio]:
        return b_b(lista, elemento, meio + 1, index_fim)

lista = [2, 3, 6, 9, 13, 14, 21, 23, 27, 35, 47, 52, 54, 69, 70, 74, 81, 87, 97, 99]
result = b_b(lista, 13, 0, 19)
print(result)