n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))
n3 = int(input("Insira mais um último número: "))
#Verificando quem é maior
if n1>n2 and n1>n3:
    print(f"O número maior é {n1}")
if n2>n1 and n2>n3:
    print(f"O número maior é {n2}")
if n3>n1 and n3>n2:
    print(f"O número maior é {n3}")
#Verificando quem é menor
if n1<n2 and n1<n3:
    print(f"O número menor é {n1}")
if n2<n1 and n2<n3:
    print(f"O número menor é {n2}")
if n3<n1 and n3<n2:
    print(f"O número menor é {n3}")
