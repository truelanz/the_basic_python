import random


class MyList(list): # Classe Pai => list
    def choice(self): # Herança, novo métoda acrescentado na classe list
        return random.choice(self)
    
l = MyList([1,4,5,6,88,13])
print(l)
print(l.choice())
