print("Vamos começar o sorteio!")
from random import choice
a1 = str(input('Insira o nome do primeiro aluno: '))
a2 = str(input('Insira o nome do segundo aluno: '))
a3 = str(input('Insira o nome do terceiro aluno: '))
a4 = str(input('Insira o nome do quarto aluno: '))
alunos = [a1,a2,a3,a4]
sorteio = choice(alunos)
print(f'O aluno sorteado foi {sorteio}')
