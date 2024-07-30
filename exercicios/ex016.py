from math import ceil, floor

def mostra_parte_inteira():
    num = float(input('Digite um numero não inteiro: '))
    novo_num = floor(num)
    return print(f' O numero {num} tem a parte inteira {novo_num}')

mostra_parte_inteira()