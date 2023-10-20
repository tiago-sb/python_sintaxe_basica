# peça um número e verifique se é positivo ou negativo

numeroUsuario = float(input("insira um número: "))
if numeroUsuario == 0:
    print("zero não é positivo nem negativo")
elif numeroUsuario > 0:
    print(numeroUsuario, " é positivo")
else:
    print(numeroUsuario, " é negativo")
