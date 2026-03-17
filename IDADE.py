nome = str(input("Informe seu nome.........: "))
nasc = int(input("Informe ano de nascimento: "))
hoje = int(input("informe ano atual........: "))
idade = hoje - nasc
print("Ola, %s" % nome)
print("Você possui em torno de %d anos de idade" % idade)