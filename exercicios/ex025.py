def verifica_nome():
    nome = str(input('Qual é o seu nome completo? ')).strip()
    res = 'Carlos' in nome.lower()
    print(f'Seu nome tem carlos? {res}')


verifica_nome()