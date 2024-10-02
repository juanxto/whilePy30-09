cont = 1
menores = 0
while cont <= 15:
    idade = int(input('Digite sua idade: '))
    if idade < 18:
        menores += 1
    cont += 1
print(f'As pessoas com menos de 18 anos são {menores}')
