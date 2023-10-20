idade = int(input("insira sua idade: "))
if idade >= 60:
    print("idoso")
elif idade >= 25 and idade < 60: 
    print("adulto")
elif idade >= 13 and idade < 25:
    print("jovem")
else:
    print("criança")
    
# [and, or, not] são os operadoes relacionais em python