""" 
Escreva a função negativos(), que aceita uma lista como entrada e exibe, um por
linha, os valores negativos na lista. A função não deverá retornar nada.
"""

# def negatives():
#    listInput = []
#    qntList = int(input('Quantos intens terá na lista? '))
#    for i in range (qntList):
#        itemList = int(input('adicione à lista: '))
#        listInput.append(itemList)
#        i += 1
#        
#    print(listInput)
#
#negatives()

def negatives(listInput):
    'Função que retorna os números negativos de uma lista'
    for numbers in (listInput):
        if numbers < 0:
            print(numbers)
        else:
            pass

negatives([1, -5, -8, 3, -6])
help(negatives)
        
    