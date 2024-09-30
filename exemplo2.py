cont = 1
aprovados = 0
reprovados = 0
while cont <= 1:
    media = float(input('Informe a media do aluno: '))
    if media >= 6:
        aprovados += 1
    else:
        reprovados += 1
    cont+=1

print(f'Quantidade de alunos aprovados: {aprovados}')
print(f'Quantidade de alunos reprovados: {reprovados}')