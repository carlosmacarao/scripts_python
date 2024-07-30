from math import sqrt


def mostra_raiz():
    num = int(input('Digite um numero: '))
    raiz = sqrt(num)
    return print(f'A raiz de {num} é igual a {raiz}')

mostra_raiz()    