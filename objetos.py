
# CRIANDO CLASSE
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def setx(self, x):
        self.x = x
        
    def sety(self,  y):
        self.y = y
        
    def get(self):
        print(self.x, self.y)
        
    def move(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety
        
    # x + y ==> (2,3) + (2,2) => (4,5)
    # x + 8 ==> (2,3) + 8 ==> (10, 11)
    def __add__(self, other):
        # Caso somar dois objetos, somar x +  x e y + y de cada objeto.
        if type(other) == Point:
            return Point(self.x + other.x, self.y + other.y)
        # Caso a soma for de um objeto com um int ou float, somar other + x e other + y
        return Point(self.x + other, self.y + other)
        
    def __repr__(self) -> str:
        return '(' + str(self.x) + ',' + str(self.y) + ')'

# CRIANDO OBJETOS    
obj01 = Point()
obj01.setx(5), obj01.sety(8)
print(obj01)

obj02 = Point(88, 99)
print(obj02)

# Utilizando função da classe
obj02.move(10, 10) 
print('# movendo', obj02)
print('# get', obj02.get())

# Utilizando sobrecarga da função __add__
obj03 = Point(3,3)
obj04 = Point(2,2)
print(obj03 + obj04)
print(obj03 + 10)

obj01.get()
