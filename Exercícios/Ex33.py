linha, consulta, ra, cpf, codigo = 0, 0, 0, 0, 0
matriz1 = [[0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, 
           [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, 
           [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, 
           [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3,]
matriz2 = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5,
           [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5,
           [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5,
           [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5, [0]*5,]
media, soma = 0.0, 0.0
situacao = ""

for linha in range(0, 40, 1):
    matriz1[linha][0] = int(input(f"Informe o RA do aluno {linha + 1}: "))
    matriz1[linha][1] = int(input(f"Informe o CPF do aluno {linha + 1}: "))
    matriz1[linha][2] = int(input(f"Informe o código do aluno {linha + 1}: "))
    matriz2[linha][0] = int(input(f"Informe a nota 1 do aluno {linha + 1}: "))
    matriz2[linha][1] = int(input(f"Informe a nota 2 do aluno {linha + 1}: "))
    matriz2[linha][2] = int(input(f"Informe a nota 3 do aluno {linha + 1}: "))
    matriz2[linha][3] = int(input(f"Informe a nota 4 do aluno {linha + 1}: "))
    matriz2[linha][4] = matriz1[linha][2]

continuar = True
while(continuar):
    print("Informe qual o tipo de consulta deseja realizar: ")
    print("1 - RA do aluno")
    print("2 - CPF do aluno")
    print("3 - Código do aluno")
    consulta = int(input("Consulta: "))
    
    encontrar = False
    if(consulta == 1):
        ra = int(input("Informe o RA do aluno: "))
        for linha1 in (matriz1):
            if(ra == linha1[0]):
                encontrar = True
                print(f"RA: {ra}")
                for linha2 in (matriz2):
                    if(linha2[4] == linha1[2]):
                        print(f"Nota 1: {linha2[0]} | Nota 2: {linha2[1]} | Nota 3: {linha2[2]} | Nota 4: {linha2[3]}")
                        soma = (linha2[0]) + (linha2[1]) + (linha2[2]) + (linha2[3])
                        media = soma / 4
                        print(f"Média: {media}")
                        if(media >= 6.0):
                            situacao = "Aprovado"
                        else:
                            if(media >= 4.0 and media < 6.0):
                                situacao = "Recuperação"
                            else:
                                if(media < 4.0):
                                    situacao = "Reprovado"
                        print(f"Situação: {situacao}")
        if(encontrar == False):
            print(f"Aluno com RA {ra} não foi encontrado na base de dados.")
    else:
        if(consulta == 2):
            cpf = int(input("Informe o CPF do aluno: "))
            for linha1 in (matriz1):
                if(cpf == linha1[1]):
                    encontrar = True
                    print(f"CPF: {cpf}")
                    for linha2 in (matriz2):
                        if(linha2[4] == linha1[2]):
                            print(f"Nota 1: {linha2[0]} | Nota 2: {linha2[1]} | Nota 3: {linha2[2]} | Nota 4: {linha2[3]}")
                            soma = (linha2[0]) + (linha2[1]) + (linha2[2]) + (linha2[3])
                            media = soma / 4
                            print(f"Média: {media}")
                            if(media >= 6.0):
                                situacao = "Aprovado"
                            else:
                                if(media >= 4.0 and media < 6.0):
                                    situacao = "Recuperação"
                                else:
                                    if(media < 4.0):
                                        situacao = "Reprovado"
                            print(f"Situação: {situacao}")
            if(encontrar == False):
                print(f"Aluno com CPF {cpf} não foi encontrado na base de dados.")        
        else:
            if(consulta == 3):
                codigo = int(input("Informe o código do aluno: "))
                for linha1 in(matriz1):
                    if(codigo == linha1[2]):
                        encontrar = True
                        print(f"Código: {codigo}")
                        for linha2 in (matriz2):
                            if(linha2[4] == linha1[2]):
                                print(f"Nota 1: {linha2[0]} | Nota 2: {linha2[1]} | Nota 3: {linha2[2]} | Nota 4: {linha2[3]}")
                                soma = (linha2[0]) + (linha2[1]) + (linha2[2]) + (linha2[3])
                                media = soma / 4
                                print(f"Média: {media}")
                                if(media >= 6.0):
                                    situacao = "Aprovado"
                                else:
                                    if(media >= 4.0 and media < 6.0):
                                        situacao = "Recuperação"
                                    else:
                                        if(media < 4.0):
                                            situacao = "Reprovado"
                                print(f"Situação: {situacao}")
                if(encontrar == False):
                    print(f"Aluno com código {codigo} não foi encontrado na base de dados.")
            else:
                print("Valor inválido.")

    opc = input("Deseja pesquisar outro aluno? ")
    if(opc.upper() ==  "S"):
        continuar = True
    else:
        if(opc.upper() == "N"):
            continuar = False
        else:
            print("Opção inválida.")
            continuar = False