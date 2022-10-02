canal = 1
porc9, porc12, porc23, porc40, porcOutros, total = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

while canal != 0:
    canal = int(input("Informe o canal (9, 12, 23 ou 40): "))

    if canal == 9:
        porc9 = porc9 + 1
    else:
        if canal == 12:
            porc12 = porc12 + 1
        else:
            if canal == 23:
                porc23 = porc23 + 1
            else:
                if canal == 40:
                    porc40 = porc40 + 1
                else:
                    if canal != 0:
                        porcOutros = porcOutros + 1

total = porc9 + porc12 + porc23 + porc40 + porcOutros

porc9 = (porc9 * 100) / total
porc12 = (porc12 * 100) / total
porc23 = (porc23 * 100) / total
porc40 = (porc40 * 100) / total
porcOutros = (porcOutros * 100) / total

print(f"A audiência do canal 9 é: {porc9:,.2f}%")
print(f"A audiência do canal 12 é: {porc12:,.2f}%")
print(f"A audiência do canal 23 é: {porc23:,.2f}%")
print(f"A audiência do canal 40 é: {porc40:,.2f}%")
print(f"A audiência dos outros canais é: {porcOutros:,.2f}%")