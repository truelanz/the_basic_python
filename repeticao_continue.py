
def primo(num):
    i = 2
    while i < num:
        # Números primos
        if num % i == 0:
            break
        i += 1
    return i == num
    
for n in range (2,100):
    # Continue até 100 sem printar caso o número não for primo
    if not primo(n):
        continue
    print(n, 'é um número primo') # printe caso for primo.