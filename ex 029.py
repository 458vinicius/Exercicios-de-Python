velocidade = float(input('Qual é a velocidade em que o carro está percorrendo? '))
if velocidade >80:
    print(f' O carro estava à {velocidade}Km/h, excedendo o limite de 80Km/h, você foi multado em R${(velocidade-80)*7:.2f}')
print(f'Parabéns, continue dirigindo com segurança!')
print('--FIM--')
