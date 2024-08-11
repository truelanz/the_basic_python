
"""" LISTAS """""

# Lista homogênea
listPets = ['dog', 'cat', 'fish']

# Lista heterogênea - mais de um 'tipo' dentro de um mesmo array
listHeterogenea = [1, 'um', [], [2, 3]]
print(listHeterogenea)
print(listHeterogenea[2])
print(1 in listHeterogenea)
print(1 not in listHeterogenea)
print(len(listHeterogenea))

# Alterando lists (lists podem ser alteradas, ao contrário de strings)
listHeterogenea[0] = 99
print(listHeterogenea)

#inserindo na posição espcífica do index. 
listHeterogenea.insert(2, 2)
print(listHeterogenea) 

# pop() -> remove e retorna ultimo elemento da lista
# remove() -> remove elemento que foi passado como parametro da lista
# sort() -> ordena a lista por oredem alfabética

""" TUPLAS """

tupleDays = ('wed', 'thur', 'fri')
print(tupleDays) # tuplas ( ) não podem ser alteradas, são imutáveis