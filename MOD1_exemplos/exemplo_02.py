# peça idade e carteira CNH
idade = int(input("insira sua idade: "))
if idade >= 18:
    carteiraMotorista = int(input("possui carteira CNH [1 - sim/2 - não]? "))
    if carteiraMotorista == 1:
        print("você pode dirigir")
    else:
        print("você não pode dirigir")
else:
    print("você não pode dirigir")