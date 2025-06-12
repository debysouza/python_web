# Imprimir os numeros a partir de um input do usuario
# ate um limite definido, tambem pelo usuario
# utilize funcao definindo parametros

inicial = int(input('Informe o valor inicial: '))
final = int(input('Informe o valor final: '))

def imprimir(inicial, final):
    for numeros in range(inicial, final+1):
        print(f'{numeros}')

imprimir(inicial, final)
