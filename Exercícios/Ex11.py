'''
Idade         Categoria
5 a 7         Infantil A
8 a 11        Infantil B
12 a 13       Juvenil A
14 a 17       Juvenil B
18 a >        Adulto
'''

nome = ""
idade = 0

nome = input("Informe o nome do nadador: ")
idade = int(input("Informe a idade do nadador: "))

if((idade >= 5) and (idade <= 7)):
    print(f"{nome}, você tem {idade} anos e está na categoria Infantil A.")
else:
    if((idade >= 8) and (idade <= 11)):
        print(f"{nome}, você tem {idade} anos e está na categoria Infantil B.")
    else:
        if((idade >= 12) and (idade <= 13)):
            print(f"{nome}, você tem {idade} anos e está na categoria Juvenil A.")
        else:
            if((idade >= 14) and (idade <= 17)):
                print(f"{nome}, você tem {idade} anos e está na categoria Juvenil B.")
            else:
                if((idade >= 18)):
                    print(f"{nome}, você tem {idade} anos e está na categoria Adulto.")
                else:
                    print(f"O nadador não possui uma categoria válida.")

