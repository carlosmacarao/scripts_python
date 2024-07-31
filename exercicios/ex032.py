from datetime import date

def ano_bissesto():

    ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

    if ano == 0:
        ano = date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano {ano} é BISSESTO')
    else:
        print(f'O ano {ano} NÃO é BISSESTO')    


ano_bissesto()