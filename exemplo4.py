while True:
    # Menu de opções

    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Sair')
    opcao = int(input('Escolha uma opção: '))

    match opcao:
        case 1:
            a = float(input('Informe um número: '))
            b = float(input('Informe outro número: '))
            print(f'Resultado da soma: {a + b}')
        case 2:
            a = float(input('Informe um número: '))
            b = float(input('Informe outro número: '))
            print(f'Resultado da subtração: {a - b}')
        case 3:
            break
        case _:
            print('Opção inválida')