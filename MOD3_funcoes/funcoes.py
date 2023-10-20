numeroUm = float(input("insira o valor 1: "))
numeroDois = float(input("insira o valor 2: "))

# função de soma
def soma(numeroUm, numeroDois):
    return numeroUm + numeroDois

print("resultado:", soma(numeroUm, numeroDois))

# função de fatorial resursivo
numeroEscolhido = int(input("insira um valor inteiro: "))
def fatorialRec(numeroEscolhido):
    if numeroEscolhido <= 1:
        return 1
    else:
        return numeroEscolhido * fatorialRec(numeroEscolhido - 1)

print("fatorial: ", fatorialRec(numeroEscolhido))    

