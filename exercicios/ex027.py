def verifica_nome():
    nome = str(input('Digite seu nome completo: ')).strip()
    nome_dividido = nome.split()
    print('Muito prazer em te conhecer!')
    print(f'Seu primeiro nome é {nome_dividido[0]}')
    print(f'Seu último nome é {nome_dividido[-1]}')


verifica_nome()    