n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))
n4 = int(input("Informe o quarto número: "))
q1 = n1**2
q2 = n2**2
q3 = n3**2
q4 = n4**2

if q3 >= 1000:
    print(q3)
    quit()
else:
    print(f"Primeiro número:{n1:>3}, Quadrado: {q1:>3}")
    print(f"Segundo número:{n2:>4}, Quadrado: {q2:>3}")
    print(f"Terceiro número:{n3:>3}, Quadrado: {q3:>3}")
    print(f"Quarto número:{n4:>5}, Quadrado: {q4:>3}")