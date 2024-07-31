def calcula_maior_numero():
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    n3 = int(input('Terceiro valor: '))

    if n1 < n2 and n1 < n3:
        menor = n1
    if n2 < n3 and n2 < n1:
        menor = n2
    if n3 < n2 and n3 < n1:
        menor = n3

    if n1 > n2 and n1 > n3:
        maior = n1
    if n2 > n3 and n2 > n1:
        maior = n2
    if n3 > n1 and n3 > n2:
        maior = n3


    print(f'O menor numero digitado foi {menor}')
    print(f'O maior numero digitado foi {maior}')    
    

calcula_maior_numero()    

