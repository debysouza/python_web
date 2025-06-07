import random
# 1-Armazene 5 frutas nas 4 estruturas (Lista/Set/Tupla/Dict)
# definir uma lista vazia
valores = []
# criar uma estrutura de repetição para inserir os 5 elementos
# for i in range(5):
#     valor = input(f'Informe a {i+1}° fruta: ')
#     valores.append(valor)
def gerar_dados(qtd, valormin, valormax):
    return [random.randint(valormin, valormax) for _ in range(qtd)]
valores = gerar_dados(8, 1, 50)
# criar uma variável para cada estrutura e fazer a devida conversão
lista_final = list(valores)
set_final = set(valores)
tupla_final = tuple(valores)
# dict_final = dict(valores) ERRO!
dict_final = {
    j: valor 
    for j, valor in enumerate(valores)
}
# imprimir os 5 resultados
print(f'Lista {lista_final}')
print(f'Set {set_final}')
print(f'Tupla {tupla_final}')
print(f'Dicionario {dict_final}')
# 2- Após o teste acima, aplique o random para inserir os valores
#na lista
