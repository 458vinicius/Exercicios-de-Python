#Uso de .strip() para tirar todos espaços digitados antes de palavras tanto na esquerda como direita
cidade = str(input('Digite o nome da sua cidade: ')).strip()
#Uso de .title() pra cada nome da cidade começar com maiúscula na hora de demonstrar
#o nome do programa no print final
#Uso de replace para substituir nomes de cidade que tenha uso de preposições que são alterados pelo .title()
tudoCaptalizado = cidade.title().replace(' Da ',' da ').replace(' Das ',' das ').replace(' De ',' de ').replace(' Do ',' do ').replace(' Dos ',' dos ').replace(" D'", " d'")
#Uso de .lower() para transformar tudo em minúsculo para ficar prático na hora
#do programa identificar a palavra "Santo" sendo digitada pelo usuário como maiúscula
#minúscula, ex: SANTO, sANto, santO;
conferir = cidade[:3].lower() == 'santo'
#Uso da lista 0 como a primeira palavra na frase.
print(f'{tudoCaptalizado} começa com a palavra "Santo"? {conferir.__str__().replace('True','Sim').replace('False','Não')}')
