# fazer uma lista de cores e printar aquelas que começam com a letra b

lista_de_cores = ["Azul", "Bege", "Gelo", "Preto", "Vinho", "Bronze", "Mostarda", "Branco", "Gris", "Bronze", "Ciano"]
for cores in lista_de_cores:
    if cores.startswith("b") or cores.startswith("B"):
        print(cores)
        