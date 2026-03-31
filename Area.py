# Usuário decide o objeto
print("\nQual área você gostaria de calcular? \n")
op = int(input("Digite (1) para Área do Retângulo ou (2) para Área do Triângulo \n"))

# Coletar dados de retângulo
altura = float (input("\nDigite o valor da altura em cm: "))
base = float (input("Digite o valor da base em cm: "))

if op == 1:

    area = base * altura
    # Imprimir resultado
    print("\nA área do Retângulo é de", area,"cm³")

else:

    area = (base * altura)/2
    # Imprimir resultado
    print("\nA área do Triângulo é de", area,"cm³")