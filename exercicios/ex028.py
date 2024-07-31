from random import randint
from time import sleep

def mensagem_inicio():
    print('-=-'*20)
    print(' Vou pensar em um numero entre 0 e 5. Tente advinhar...')
    print('-=-'*20)


def escolha_numero():
    computador = randint(0, 5)
    jogador = int(input('Em que numero eu pensei? '))
    print('PROCESSANDO...')
    sleep(2)
    if jogador == computador:
        print('PARABÉNS! Voce conseguiu me vencer!')
    else:
        print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')


mensagem_inicio()    
escolha_numero()
#mensagem_fim()
