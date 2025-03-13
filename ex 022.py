#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()
divisaoNome = nome.split()
print(f'''O seu nome em letras maiúsculas fica: {nome.upper()}
O seu nome em letras minúsculas fica: {nome.lower()}
Seu nome completo possui {len(nome.replace(" ", ""))} letras!
Seu primeiro é {divisaoNome[0]} e possui {len(divisaoNome[0])} letras!
''')
