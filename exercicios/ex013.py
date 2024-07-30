nome = input('Nome do funcionario: ')

sal = float(input('Salário atual: '))

aumento = sal * 0.15
novo_sal = sal + aumento

print('\n Salário atual do {}: {}. \n Com aumento de 15% seu novo salário será: {}.'.format(nome, sal, novo_sal))