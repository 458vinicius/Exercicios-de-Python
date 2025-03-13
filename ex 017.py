from math import hypot
cO = float(input('Insira o comprimento do cateto oposto: '))
cA = float(input('Insira o comprimento do cateto adjascente: '))
print(f'O valor da hipotenusa é de {hypot(cO,cA):.2f} ')
