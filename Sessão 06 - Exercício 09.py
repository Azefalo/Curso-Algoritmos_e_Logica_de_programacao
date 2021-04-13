poluicao = float(input("Informe o índice de poluição: "))
if poluicao >= 0.3 and poluicao < 0.4:
    print("Atenção: Indústrias do grupo 01 deve suspender atividades")
elif poluicao >= 0.4 and poluicao < 0.5:
    print("Atenção: Indústrias do grupo 01 e indústrias do grupo 02 devem suspender atividades")
elif poluicao >= 0.5:
    print("Atenção: Todos os grupos de indústrias devem suspender atividades")
else:
    print("Níveis aceitáveis")