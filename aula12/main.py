
def elif_test():
    hora = 119

    print(f'Agora sÃo {hora} horas.')

    if hora >= 0 and hora < 12:
        print('Bom dia!')
    elif hora >= 12 and hora < 18:
        print('Boa tarde!')   
    else:
        print('Boa noite!')     