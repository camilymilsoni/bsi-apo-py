
tc = ""
ct = 0.0
valor = 0.0
combust = 0.0

tc = input("Informe o tipo do carro (G - gasolina ou A - álcool): ")
ct = float(input("Informe a capacidade do tanque em litros: "))

tc = tc.upper()

if(tc == "G"):
    print(f"O tipo do carro é: 'Gasolina'")
else:
    print(f"O tipo do carro é: 'Álcool'")

combust = float(input("Informe o valor do preço do litro do combustível: R$"))
valor = combust * ct
print(f"O valor para encher o tanque de combustível é: R${valor:,.2f}")
