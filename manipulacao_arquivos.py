""" Os arquivos são armazenados na memória secundária do PC (HDD, SSD, etc) - Memórias não voláteis """

# Função para ler arquivos de texto, separando palavras e visualizar a quantidade de palavras e caracteres.
def readFile(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordList = content.split()
    print(wordList)
    return len(wordList), len(content)

n_words, n_chars = readFile('test.txt')
print(n_words)
print(n_chars)

# Sobrescrever arquivos:
def WriteAndReadFile(filename, content):
    try:
        # Abre o arquivo no modo de escrita (cria o arquivo se não existir)
        with open(filename, 'w') as arquivo:
            arquivo.write(content)
            print(f"Conteúdo escrito no arquivo '{filename}' com sucesso.")
        
        # Abre o arquivo novamente no modo de leitura e imprime o conteúdo
        with open(filename, 'r') as readFile:
            readContent = readFile.read()
            print(f"Conteúdo do arquivo '{filename}':\n{readContent}")
    except Exception as error:
        print(f"Erro ao escrever no arquivo: {error}")

# Exemplo de uso:
filename = "myFile.txt"
writeText = "This is just a text and works"

WriteAndReadFile(filename, writeText)



