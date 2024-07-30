from math import hypot

def comprimento_hipotenusa():
    co = float(input('Comprimento do cateto oposto: '))
    ca = float(input('Comprimento do cateto adjacente: '))
    hi = hypot(co, ca)
    print(f'A hipotenusa vai medir {hi:.2f}')


comprimento_hipotenusa()    
