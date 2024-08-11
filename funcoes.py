""" Definição de funções """

# f(x) = x^2 + 1

def f(x):
    res = x**2+1
    return res

f(7)


# ESTRUTURA DA FUNÇÃO

# def <nome_funcao>(<parametro>):
    #<instrução>
    #...
    #...
    #return <variavel/valor> (opcional)

def juros(preco, juros):
    res = preco * (1 + (juros / 100))
    return res

juros(10, 50)

