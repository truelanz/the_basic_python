def maior(lista):
    maximo = lista[0] # max = 2
    for num in lista: # para cada elemento da lista
        if num > maximo: # caso o número da vez do loop for for maior que anterior
            maximo = num # esse número será o novo "máximo"
    return maximo

list = [2,5,8,3,1,18,55,1,0,6]
print(maior(list))