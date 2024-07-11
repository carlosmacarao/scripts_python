nome = input('Nome do Aluno: ')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

print('A média das notas do Aluno {} é {:.2f}'.format(nome, media))