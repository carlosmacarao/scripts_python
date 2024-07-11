preco = float(input('Preço atual do produto: '))

desconto = preco * 0.05
novo_preco = preco - desconto

print('\n Preço atual: {}. \n Novo preço: {}'.format(preco, novo_preco))