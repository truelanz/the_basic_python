""" 
Implemente a função perímetro(), que aceita, como entrada, o raio de um círculo
(um número não negativo) e retorna o perímetro do círculo.
"""

"""
C = 2 * π * r, onde:

C = comprimento da circunferência ou perímetro.
π = 3,14 (aproximadamente)
r = raio da circunferência (medida do centro à extremidade) 
"""

def perimeter(r):
    pi_ = 3.14
    res = 2 * pi_ * r
    return print('O perímetro do círculo é:', res)

perimeter(0.4)
    