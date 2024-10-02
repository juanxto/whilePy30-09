cont = 1
while cont <= 2:
    if cont == 1:
        n1 = int(input('Digite um valor: '))
    if cont == 2:
        n2 = int(input('Digite um valor: '))
    cont += 1
if n1 > n2:
    print(f'O maior valor digitado foi {n1}')
else:
    print(f'O maior valor digitado foi {n2}')