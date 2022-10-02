linha = 0
coluna = 0
mat = [[""]*3, [""]*3, [""]*3]

for linha in range(0,3,1):
    for coluna in range(0,3,1): 
        mat[linha][coluna] = input(f"Informe o texto para a posição {linha} {coluna}: ")

for linha in range(0,3,1):
    for coluna in range(0,3,1): 
        print(f"[{mat[linha][coluna]}]", end= '')
    print()