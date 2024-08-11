
def bubble_sort(v):
    for i in range(len(v)-1): #Percorrendo a Matriz 
        for j in range(len(v)-i-1): #Percorrendo a Matriz 
            if(v[j] > v[j+1]): #Se o elemento da esquerda for maior que o da direita
                v[j], v[j+1] = v[j+1], v[j] # inverte suas posições
                         
    
mat = [5,99,22,55,4,3,88,7,44,6,11]
print(f'Lista não ordenada: {mat}')
bubble_sort(mat)
print(f'Lista ordenada | BUBBLE SORT: {mat}')