r1 = float(input("Insira o comprimento de uma reta: "))
r2 = float(input("Insira o comprimento de outra reta: "))
r3 = float(input("Insira o comprimento de mais outra reta: "))
if (r1+r2)>r3 and (r1+r3)>r2 and (r2+r3)>r1:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')
