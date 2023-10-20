# crie uma tupla com nome de frutas peça pro usuário digitar uma fruta 
# e verifique se aquela fruta se encontra na tupla

nome_frutas = ("Abacate", "Bacaba", "Cacau", "Caqui", "Carambola", "Cereja", "Goiaba", "Jaca", "Jambo")
fruta_escolhida =str(input("insira uma fruta: "))
if fruta_escolhida in nome_frutas:
    print("a fruta se encontra na tupla! :)")
else:
    print("a fruta não se encontra na tupla! :(")