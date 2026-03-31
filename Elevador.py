capacidade =  float(input("Digite a capacidade do elevador: "))
peso1 = float(input("Digite o peso da 1ª pessoa: "))
peso2 = float(input("Digite o peso da 2ª pessoa: "))
peso3 = float(input("Digite o peso da 3ª pessoa: "))
peso4 = float(input("Digite o peso da 4ª pessoa: "))
peso5 = float(input("Digite o peso da 5ª pessoa: "))

pesoTotal = peso1 + peso2 + peso3 + peso4 + peso5
if pesoTotal >= capacidade:
    print("Carga máxima permitida do elevador excedida!")
else:
    print("Elevador liberado para subir!")