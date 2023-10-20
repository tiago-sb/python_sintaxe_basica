import math
import random

valorEscolhido = float(input("insira um valor: "))
print("raiz quadrada:", math.sqrt(valorEscolhido)) # sqrt, calcula a raiz quadrada de um valor

# round, função que fixa a quantidade de casas após a vírgula
print("seno:", round(math.sin(valorEscolhido), 3)) # sin, calcula o seno do valor escolhido
print("seno:", round(math.cos(valorEscolhido), 2)) # cos, calcula o cosseno do valor escolhido

# randint, função para gerar números aleatórios entre um determinado intervalo definido
numero_aleatorio = float(random.randint(1, 100))
print("número aleatório:", numero_aleatorio)
