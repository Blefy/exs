"""
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
"""
height=float(input("Insira sua altura."))
peso_ideal_masculino=(72.7*height) - 58
peso_ideal_feminino=(62.1*height) - 44.7
print(f"o peso ideal para homens é {peso_ideal_masculino:.2f}kg. " 
    f"o peso ideal para mulheres é {peso_ideal_feminino:.2f}kg."
    )