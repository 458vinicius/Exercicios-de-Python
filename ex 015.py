# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km
# rodado.
km = float(input("Quantos Km foram percorridos com o carro? "))
d = int(input("Quantos dias foram alugados? "))
v= (km*0.15)+(d*60)
print(f"O valor total do aluguel a ser pago será de R${v:.2f}")
