cont = 1
pares = 0
while cont <= 10:
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        pares += 1
    cont +=1
print(f'Quantidade de números pares: {pares}')