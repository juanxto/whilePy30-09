numdigit = 0
while True:
    n = int(input("Digite um numero(Digite 0 para finalizar o programa): "))
    if n == 0:
        break
    else:
        numdigit += n
print(f'A soma de todos os numeros digitados foi de {numdigit}')