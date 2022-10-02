
horasTrab, depend, horasExt, gratificacao = 0, 0, 0, 0
salarioMin, valorH, salarioMes, dep, vHorasExt, salarioB, imposto, salarioLiq, salarioRec = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

salarioMin = float(input("Digite o valor do salário mínimo: R$"))
horasTrab = int(input("Digite o número de horas inteiras trabalhadas: "))
depend = int(input("Digite o número de dependentes do funcionário: "))
horasExt = int(input("Digite a quantidade de horas extras inteiras trabalhadas: "))

valorH = salarioMin / 5
salarioMes = horasTrab * valorH
dep = 32 * depend
vHorasExt = (valorH * 1.5) * horasExt
salarioB = salarioMes + vHorasExt + dep

if(salarioB < 200):
    imposto = 0.0
else:
    if(salarioB >= 200) and (salarioB <= 500):
        imposto = 0.1 * salarioB
    else:
        imposto = 0.2 * salarioB

salarioLiq = salarioB - imposto

if(salarioLiq <= 350):
    gratificacao = 100
else:
    gratificacao = 50

salarioRec = salarioLiq + gratificacao
print(f"O salário a receber é: R${salarioRec:,.2f}")