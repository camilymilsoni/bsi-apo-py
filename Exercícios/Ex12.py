'''
Salário                 Bonificação
Até R$500                 5%
Entre R$500 e R$1200      12%
Acima de R$1200           0%

Salário             Auxílio Escola
Até R$600            R$150
Mais que R$600       R$100
'''

salario = 0.0
salarioF = 0.0
bonus = 0.0
aux = 0.0

salario = float(input("Informe o salário do funcionário: R$"))

if(salario <= 500):
    bonus = 0.05 * salario
else:
    if ((salario > 500) and (salario <= 1200)):
        bonus = 0.12 * salario
    else:
            bonus = 0.0

if(salario <= 600):
    aux = 150
else:
    aux = 100

salarioF = salario + bonus + aux

print(f"O novo salário, acrescido de bonificação e auxílio escola, é: R${salarioF:,.2f}")
