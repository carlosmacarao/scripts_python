from math import radians, sin, cos, tan

def seno_cosseno_tangente():
    angulo = float(input('Digite o angulo que deseja: '))
    seno = sin(radians(angulo))
    coseno = cos(radians(angulo))
    tangente = tan(radians(angulo))

    print(f'O angulo de {angulo} tem o SENO {seno:.2f}')
    print(f'O angulo de {angulo} tem o COSSENO {coseno:.2f}')
    print(f'O angulo de {angulo} tem a TANGENTE {tangente:.2f}')


seno_cosseno_tangente()    