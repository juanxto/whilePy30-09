cont = 1
num = 0
while cont <= 10:
    numeros = float(input('Digite um numero: '))
    if numeros >= 100 and numeros <= 200:
        num += 1
    cont += 1
print(f'A quantidade de numeros entre 100 e 200 entre os numeros digitados foram {num}')