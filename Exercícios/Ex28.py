'''
Criar um algoritmo que leia os elementos de uma matriz inteira 5 x 5 e escreva os elementos da diagonal principal.
OBS: Para ler a matriz e imprimir a diagonal principal deve ser utilizado o comando FOR.
'''

linha = 0
coluna = 0
mat = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]

for linha in range(0,5,1):
    for coluna in range (0,5,1):
        mat[linha][coluna] = int(input(f"Informe o número para a posição {linha} {coluna}: "))

print("Matriz inteira 5 x 5: ")

for linha in range(0,5,1):
    for coluna in range (0,5,1):
        print(f"[{mat[linha][coluna]}]", end= '')
    print()

print("Matriz apenas com os elementos da diagonal principal: ")

for linha in range(0,5,1):
    for coluna in range (0,5,1):
        if (linha == coluna):
            print(f"[{mat[linha][coluna]}]", end= '')
    print()
