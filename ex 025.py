nome = str(input("Digite o nome completo de alguma pessoa: ")).strip()
#Uso de .title() pra cada nome da pessoa começar com maiúscula na hora de demonstrar
#o nome do programa no print final
#Uso de replace para substituir nomes de pessoas que tenha uso de preposições que são alterados pelo .title()
tudoCapta = nome.title().replace(' Da ',' da ').replace(' Das ',' das ').replace(' De ',' de ').replace(' Do ',' do ').replace(' Dos ',' dos ').replace(" D'", " d'")
#Uso de .lower() para transformar tudo em minúsculo para ficar prático na hora
#do programa identificar o nome "Silva" sendo digitada pelo usuário como maiúscula
#minúscula, ex: SILVA, sIlVa, silvA,etc.
nomeMinusculo = nome.lower()
conferir = "silva" in nomeMinusculo
print(f"O nome {tudoCapta} tem 'Silva'? {conferir.__str__().replace('True','Sim').replace('False','Não')}")
