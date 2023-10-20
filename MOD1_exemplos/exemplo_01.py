# peça um número inteiro e imprima na tela se o número é par ou impar

numeroUsuario = int(input("insira um número: "))
print(numeroUsuario % 2 == 0 and "par" or "impar")