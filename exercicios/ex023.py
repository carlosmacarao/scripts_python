def analisa_numero():
    num = input('Informe um numero: ')
    
    print(f'Unidade: {num[-1]}')
    print(f'Dezena: {num[-2]}')
    print(f'Centena: {num[1]}')
    print(f'Milhar: {num[0]}')

analisa_numero()    