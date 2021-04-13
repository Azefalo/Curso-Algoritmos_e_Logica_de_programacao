altura = float(input("Informe sua altura: "))
sexo = input("Informe seu sexo(M ou F): ")
if sexo == "M" or sexo == "m":
    print(f"Seu peso ideal é {72.7 * altura - 58:.2f}")    
elif sexo == "F" or sexo == "f":
    print(f"Seu peso ideal é {62.1 * altura - 44.7:.2f}")
else:
    print("Sexo não reconhecido")