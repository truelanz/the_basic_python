
class Stack():
    def __init__(self):
        self.data = []
        
    def push(self, x):
        self.data.append(x)
        
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)
        
    def top(self):
        if len(self.data) > 0:
            return self.data(-1)
        
    def empty(self):
        return not len(self.data) > 0
    
    def __repr__(self):
        return (f'stack: {self.data}')
    
pilha = Stack()

pilha.push(4), pilha.push(5), pilha.push(6)

print(pilha)

print(pilha.pop())
print(pilha.pop())

print(pilha)

"Conversão de decimal para binário usando Pilha"

dec = Stack()
num = 13
while num > 0:
    rest = num % 2 # resto - 1, 0, 1, 1
    num = num // 2 # Divisão absoluta, para saber qual o proximo número que deve ser calculado o resto. - 13, 6, 3, 1
    dec.push(rest)
    
while not dec.empty():
    dec_to_bin = dec.pop()
    print(f'{dec_to_bin}', end=" ")