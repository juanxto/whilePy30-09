cont = 0
soma = 0


while True:
    idade = int(input('Informe a idade (digite -1 para finalizar): '))
    if idade < 0:
        break
    soma += idade
    cont += 1

media = soma / cont
print(f'Média das idades: {media}')