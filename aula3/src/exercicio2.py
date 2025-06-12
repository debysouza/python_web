# Imprima uma contagem regressiva com input de partida feito
# pelo usuario
# utilize while e funcao
import time

partida = int(input('Informe o valor de partida: '))

def contador(partida):
    while partida >= 0:
        print(f'{partida}')
        time.sleep(1)
        partida -= 1

contador(partida)
