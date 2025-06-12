# Conte quantas vezes o usuario interagiu ate digitar a 
# opcao de sair
# utilize funcao, while e crie um menu com 3 opcoes

menu = ['1. Lista', '2. Produto', '3. Sair']

def contador_menu(menu):
    contador = 0
    while True:
        print(menu)
        opcao = int(input('Informe uma opção: '))
        if opcao == 3:
            print(contador)
            break
        else:
            contador += 1

contador_menu(menu)
