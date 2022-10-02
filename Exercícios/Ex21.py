cont = 0
vet = [0.0]*5

for cont in range(0,5,1):
    vet[cont] = float(input(f"Informe o número para a posição {cont}: "))

for cont in range(0,5,1):
    print(f"[{vet[cont]}]", end= ' ')