e = 0
m = 0
peso = float(input("Informe o peso dos peixes: "))
if peso > 50:
    print(f"Você deverá pagar R${(peso - 50) * 4:.2f}")
else:
    print(f"Multas: {m}")
    print(f"Excesso: {e}")