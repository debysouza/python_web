# definir um dicionario com 3 elementos
dicionario = {
    'nome': 'Débora Souza',
    'cpf': '123456789-11',
    'telefone': '24999995566'
}
# adicionar um elemento (chave/valor)
dicionario['senha'] = 'ddd123'
print(dicionario)
# alterar um valor de um chave específica
dicionario.update({'login': 'deby', 'telefone':'24911112222', 'nome': 'Rafael'})
dicionario['telefone'] = '24933221100'
print(dicionario)
# remover um elemento (chave/valor)
del dicionario['telefone']
print(dicionario)
