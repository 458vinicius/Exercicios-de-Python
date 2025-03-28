from random import randint
from time import sleep
print('-=-'*20)
print('   Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
num = randint(0,5)
numUsuario = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if numUsuario == num:
    print('Parabéns! Você ganhou!')
else:
    print(f'Você perdeu, eu pensei no número {num}, não no número {numUsuario}! ')
