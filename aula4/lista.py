# definir uma lista com 3 elementos
lista = ['RJ', 'SC', 'MG']
# acessar por índice
print(lista[1])
# alterar por índice
lista[2] = 'SP'
print(lista)
# adicionar
lista.append('AC')
print(lista)
# adicionar por índice
lista.insert(0, 'RR')
print(lista)
# remover por valor
lista.remove('SP')
print(lista)
# remover por índice
del lista[2]
print(lista)
lista.pop(1)
print(lista)