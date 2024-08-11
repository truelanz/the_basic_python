""" Função para sequencia de Fibonacci
num + num_anterior """

def fibonacci(n):
    if n <= 0:
        return "O número deve ser maior que zero."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

print(fibonacci(8))