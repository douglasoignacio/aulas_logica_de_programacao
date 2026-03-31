# Usuário decide o objeto
print("\nQual volume você gostaria de calcular? \n")
escolha = int(input("Digite (1) para Lata de Óleo ou (2) para Caixa de Papelão \n"))

if escolha == 1:
    # Coletar dados de lata
    altura = float (input("\nDigite a altura da lata de óleo em cm: "))
    raio = float (input("Digite o raio da lata de óleo em cm: "))

    # Calculo
    volumelata = 3.14159 * raio**2 * altura
    # Imprimir resultado
    print("O volume da Lata de Óleo é de", volumelata,"cm³")

else:
    # Coletar dados de caixa
    altura = float (input("\nDigite a altura da caixa de papelão em cm: "))
    largura = float (input("Digite a largura da caixa de papelão em cm: "))
    comprimento = float (input("Digite o comprimento da caixa de papelão em cm: "))

    # Calculo
    volumecaixa = altura * largura * comprimento
    # Imprimir resultado
    print("O volume da caixa de Papelão é de", volumecaixa,"cm³")