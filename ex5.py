cont = 1
numimpar = 0
while cont <= 15:
    n = float(input('Digite um numero: '))
    if n % 2 != 0:
        numimpar += n
    cont += 1
print(f'A soma de todos os números impares digitados é {numimpar}')