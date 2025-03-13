#  Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
a = float(input('Insira o valor de um ângulo em graus: '))
r = radians(a)
seno = sin(r)
cosseno = cos(r)
tangente = tan(r)
print(f'O seno desse angulo é de {seno:.2f}, o cosseno é de {cosseno:.2f} e a tangente é de {tangente:.2f}')
