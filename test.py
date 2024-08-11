

atual = 100
porc = 0.05

for i in range(0, 20):
    sobra = atual * porc
    auxiliar = atual - sobra
    atual = auxiliar
    
print(atual)