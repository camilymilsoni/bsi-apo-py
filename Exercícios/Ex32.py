'''
Faça um algoritmo que receba 5 números e ao final mostre quem é o maior e o menor número digitado.
Deve-se fazer uma função para verificar o maior e outra para verificar o menor.
O menor e o maior número devem ser retornados para o programa principal para, então, serem mostrados.
'''

num = 0
cont = 0
mai = 0
men = 999999

def fMaior(numero, maior):

    if(numero > maior):
        maior = numero
    return maior

def fMenor(numero, menor):

    if(numero < menor):
        menor = numero
    return menor

for cont in range(0,5,1):
    num = int(input("Informe um número: "))
    mai = fMaior(num, mai)
    men = fMenor(num, men)

print(f"O maior número digitado é: {mai}")
print(f"O menor número digitado é: {men}")