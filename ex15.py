

ganho_por_hora=float(input("Quanto ganha por hora trabalhada?"))
numero_hora_mes=float(input("Quantas horas trabalhadas no mês?"))

salario=ganho_por_hora*numero_hora_mes
print(f"seu salario é de {salario:.2f}R$")

IR=salario*0.11
INSS=salario*0.08
sindicato=salario*0.05
salario_liquido=salario-IR-INSS-sindicato

print(f"IR {IR:.2f}R$ INSS {INSS:.2f}R$ Sindicato {sindicato:.2f}R$ e o salario liquido {salario_liquido:.2f}R$")

