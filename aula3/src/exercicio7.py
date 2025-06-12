# Crie uma funcao para imprimir a sequencia de Fibonacci
# com até N termos, definido pelo usuario
# 0 1 1 2 3 5 8

termos = int(input('Informe quantos termos deseja: '))

def fibonacci(termos):
    lista = []
    a, b = 0, 1
    while len(lista) < termos:
        lista.append(a)
        a, b = b, a+b
    print(lista)

fibonacci(termos)