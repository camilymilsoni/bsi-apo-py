'''
Criar um algoritmo que leia 10 números pelo teclado e exiba os números na ordem inversa da que os números foram digitados.
'''

cont = 0
vet = [0]*10

for cont in range(0,10,1):
    vet[cont] = int(input("Informe o número: "))

print("Na ordem inversa: ")

for cont in range(0,10,1):
    print(f"{vet[9-cont]}")