sal = float(input("Qual o salário do funcionário: R$"))
if sal>1250:
    print(f"Com aumento, o valor ficará de R${sal+(sal*0.10):.2f} ")
else:
    print(f"Com aumento, o valor ficará de R${sal+(sal*0.15):.2f}")
