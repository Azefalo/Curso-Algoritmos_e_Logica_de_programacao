n = int(input("Informe um número: "))
if n % 2 == 0:
    if n > 0:
        print(f"O número {n} é par e positivo")
    else:
        print(f"O número {n} é par e negativo")
else:
    if n > 0:
        print(f"O número {n} é ímpar e positivo")
    else:
        print(f"O número {n} é ímpar e negativo")