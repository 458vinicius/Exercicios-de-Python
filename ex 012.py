p = float(input('Insira o preço de um produto: R$'))
cal = (5/100)*p
d = p-cal
print(f'Na liquidação de 5% de desconto o produto ficará por R${d:.2f}')
