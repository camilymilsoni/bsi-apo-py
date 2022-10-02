#Faça um programa que receba o salário base de um funcionário. 
#Calcule e mostre o salário a receber, sabendo que esse funcionário tem
#gratificação de R$50 e paga imposto de 10% sobre o salário base.

salario = 0.0
imposto = 0.0
salarioF = 0.0

salario = float(input("Informe o salário: R$"))

imposto = 0.1 * salario
salarioF = salario + 50 - imposto

print(f"O salário a receber é: R$ {salarioF}")