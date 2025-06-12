# Imprima uma tabuada escolhida pelo usuario
# utilize time, funcao e for
import time

tabuada = int(input('Informe a tabuada que deseja: '))

def calculo(tabuada):
    for i in range(0, 11):
        print(f'{i} x {tabuada} = {i*tabuada}')
        time.sleep(1)

calculo(tabuada)
