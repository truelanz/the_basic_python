""" Dada uma determinada Matriz, retornar Matriz transposta """

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def transposta(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    matriz_transposta = []
    
    for j in range (colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(matriz[i][j])
        matriz_transposta.append(nova_linha)
        
    return matriz_transposta

matriz_transposta = transposta(matriz)

print("Matriz Transposta: ")
for linha in matriz_transposta:
    print(linha)