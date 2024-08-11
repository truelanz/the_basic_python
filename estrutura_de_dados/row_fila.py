class Row():
    def __init__(self):
        self.data = []
        
    def insert(self, x):
        self.data.append(x)
        
    def remove(self):
        if len(self.data) > 0: 
            return self.data.pop(0)
        else:
            print('A Fila está vazia, não é possível remover o elemento')
        
    def isEmpty(self): # Retorna verdadeiro caso a lista estiver vazia
        return not len(self.data) > 0
    
    def top(self):
        if len(self.data) > 0:
            return self.data[0]
        
    def __len__(self):
        return len(self.data)
        
    def __repr__(self) -> str:
        return (f'row: {self.data}')
        
fila = Row()
fila.insert(1), fila.insert(2), fila.insert(3)
print(fila)
print(fila.remove())
print(fila.isEmpty())


""" 
fila normal e fila prioritária:
O programa deverá permitir que pessoas
sejam inseridas no fim de cada fila,
dependendo da idade de cada uma (acima de
60 anos entra na fila prioritária).

A cada duas pessoas que
saem da fila prioritária, uma sai da fila normal. 
"""

# Iniciando objetos
fila_prioritaria = Row()
fila_normal = Row()

# Perguntando a idade das pessoas, e colocando elas na fila de acordo com a idade.
f = 0
while f < 10:
    idade = eval(input('Quantos anos você tem?'))
    if idade > 60:
        fila_prioritaria.insert(idade)
    else:
        fila_normal.insert(idade)
    f += 1
        
print(fila_prioritaria)
print(fila_normal)

# armazenando tamanho total da fila
tam_filas = len(fila_normal) + len(fila_prioritaria)
r = tam_filas
print(f'Tamanho das filas ao todo: {tam_filas}')

# removendo as pessoas da fila de acordo com a idade, e atualizando o tamanho da fila.
while r != 0:
    if len(fila_prioritaria) >= 2 and len(fila_normal) > 0:       
        fila_prioritaria.remove(), fila_prioritaria.remove()
        fila_normal.remove()
        print(f'Fila prioritaria: {fila_prioritaria}, Fila normal: {fila_normal}')
        tam_filas = len(fila_normal) + len(fila_prioritaria)
        print(f'Tamanho das filas ao AGORA: {tam_filas}')
    elif len(fila_prioritaria) == 1 and len(fila_normal) > 0:
        fila_prioritaria.remove()
        fila_normal.remove()
        print(f'Fila prioritaria: {fila_prioritaria}, Fila normal: {fila_normal}')
        tam_filas = len(fila_normal) + len(fila_prioritaria)
        print(f'Tamanho das filas ao AGORA: {tam_filas}')
    elif fila_prioritaria.isEmpty() and len(fila_normal) > 0:
        fila_normal.remove()
        print(f'Fila prioritaria: {fila_prioritaria}, Fila normal: {fila_normal}')
        tam_filas = len(fila_normal) + len(fila_prioritaria)
        print(f'Tamanho das filas ao AGORA: {tam_filas}')
    r = tam_filas
