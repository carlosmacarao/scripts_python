def calcula_media():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))

    m = (n1 + n2) / 2

    print(f'Sua média foi {m:.2f}')

    if m >= 12:
        print(f'Sua média foi boa! PARABÉNS!')
    else: 
        print('Sua média foi ruim! ESTUDE MAIS!')   

    #print('PARABÉNS' if m >= 10 else 'ESTUDE MAIS')    CONDIÇÃO SIMPLIFICADA

calcula_media()    