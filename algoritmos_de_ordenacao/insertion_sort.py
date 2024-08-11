
def insertion_sort(array):
    for i in range(1,len(array)): # para cada elemento do segundo ao tamanho total da lista
        b = i
        while b > 0 and array[b-1] > array[b]: # [...] enquanto o elemento da direita for menor que o da esquerda
            array[b-1], array[b] = array[b], array[b-1] # subistitui o da direita para a esquerda
            b -= 1 # até não houver mais maiores que o numero armazenado à esquerda
            
l = [ 11,1,55,7,6,4,88,2,102]
print(f'lista não ordenada: {l}')
insertion_sort(l)
print(f'lista ordenada | INSERTION SORT: {l}')