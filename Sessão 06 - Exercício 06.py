e = 0
c = int(input("Informe o código: "))
n = int(input("Informe a quantidade de horas trabalhadas: "))
if n > 50:
    e = n - 50
    n = n - e
print(f"Salário Total: R${n*10+e*20}")
print(f"Valor excedente: R${e*20:.2f}")