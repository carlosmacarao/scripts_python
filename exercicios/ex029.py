
def calcula_velocidade():
    v = float(input('Qual é a velocidade atual do carro? '))
    multa = (v-80) * 7
    if v <= 80:
        print('Tenha um bom dia! Dirija com segurança!')
    else:
        print(f'MULTADO! Voce excedeu o limite permitido que é de 80Km/h')   
        print(f'Voce deve pagar uma multa de {multa}MT!')
        print('Tenha um bom dia! Dirija com segurança!') 

calcula_velocidade()        