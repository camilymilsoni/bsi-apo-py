'''
Calcular a quantidade de litros de combustível gastos em uma viagem. Para obter o
cálculo, o usuário deverá fornecer o tempo gasto, quantos km/L o carro faz e a velocidade
média durante a viagem. O programa deverá apresentar os valores da velocidade média,
tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizados na viagem.
'''

tempo, kmL, velM, dist, lit = 0.0, 0.0, 0.0, 0.0, 0.0

tempo = float(input("Digite o tempo gasto (em horas) na viagem: "))
kmL = float(input("Digite quantos km/L o carro faz: "))
velM = float(input("Digite a velocidade média (km/h) durante a viagem: "))

dist = tempo * velM
lit = dist / kmL

print(f"A velocidade média foi: {velM}km/h")
print(f"O tempo gasto na viagem foi: {tempo}h")
print(f"A distância percorrida foi: {dist}km")
print(f"A quantidade de litros utilizados na viagem foi: {lit}L")