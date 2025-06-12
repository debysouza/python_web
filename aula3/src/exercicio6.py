# Crie uma funcao para verificar palindromo e retorne
# verdadeiro ou falso

palavra = input('Digite uma palavra: ')

def verifica_palindromo(palavra):
    if palavra == palavra[::-1]:
        return True
    else:
        return False

print(verifica_palindromo(palavra))