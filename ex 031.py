distancia = float(input("Qual será a distância da sua viagem em Km: "))
preço = distancia*0.50 if distancia<=200 else distancia*0.45
print(f"Sua viagem custará R${preço:.2f}")
