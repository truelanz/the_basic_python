""" Conversão de Base - Binária para Decimal """

# executar comandos no sistema operacional
""" import subprocess
 
tmo = subprocess.run('timeout 5', shell=True)
cls = subprocess.run('cls', shell=True) """

numero_decimal = int(input('Digite um número decimal: '))

numero_binario = str('')

# Enquanto o número decimal não for zero, continue dividindo por 2
while numero_decimal > 0:
    # Verifique se há resto na divisão
    resto = numero_decimal % 2
    if resto:
        # Se houver resto, adicione '1' à esquerda do número binário
        numero_binario = '1' + numero_binario
    else:
        # Se não houver resto, adicione '0' à esquerda do número binário
        numero_binario = '0' + numero_binario
    # Atualize o número decimal para o próximo passo da divisão
    numero_decimal //= 2 # numero_decimal é igual ao número decimal dividido por 2


print("O número binário é:", numero_binario)