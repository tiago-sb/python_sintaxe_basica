# criando minha lista de strings
minha_lista = ["tiago","ana","flávia","felipe"]

#acessando os elementos da minha lista
elemento_01 = minha_lista[0]
elemento_02 = minha_lista[1]
elemento_03 = minha_lista[2]
elemento_04 = minha_lista[3]

# exibição dos resultados
print("elemento 1:", elemento_01)
print("elemento 2:", elemento_02)
print("elemento 3:", elemento_03)
print("elemento 4:", elemento_04)

#listas possuem diversas funções em conjunto a ela
# tamanho da lista, onde a lista vai como parâmetro -> len(lista)
print("tamanho da minha lista", len(minha_lista))

# adicionar valores à lista -> lista.append()
minha_lista.append("júlia")
for posicaoLista in minha_lista:
    print("aluno: ", posicaoLista)
    
# remover valores da lista -> lista.remove(elemento)
minha_lista.remove("flávia")
for posicaoLista in minha_lista:
    print("aluno: ", posicaoLista)
    
# ordenar os elementos de forma crescente -> lista.sort()
minha_lista_segunda = [1, 7, 8, 3, 6, 2, 8]
minha_lista_segunda.sort()
print(minha_lista_segunda)
 