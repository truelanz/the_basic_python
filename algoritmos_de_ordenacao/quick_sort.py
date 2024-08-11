def quick_sort(lista, inicio, fim):
    if inicio < fim:
        indice_pivo = particao(lista, inicio, fim)
        quick_sort(lista, inicio, indice_pivo - 1)
        quick_sort(lista, indice_pivo + 1, fim)

def particao(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i+1], lista[fim] = lista[fim], lista[i+1]
    return i + 1

# Testando a função
lista = [54,26,93,17,77,31,44,55,20]
quick_sort(lista, 0, len(lista)-1)
print(lista)