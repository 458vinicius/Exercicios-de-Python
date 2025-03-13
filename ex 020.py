print('Vamos começar a ordem de sorteio')
a1 = str(input('Qual o nome do primeiro aluno: '))
a2 = str(input('Qual o nome do segundo aluno: '))
a3 = str(input('Qual o nome do terceiro aluno: '))
a4 = str(input('Qual o nome do quarto aluno: '))

from random import shuffle

alunos = [a1,a2,a3,a4]
shuffle(alunos)

for indice, aluno in enumerate(alunos, start=1):
    print(f'{indice}º- {aluno}')
