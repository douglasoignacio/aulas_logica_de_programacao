salario = float(input("Digite o salário: R$ "))
reajuste = float(input("Digite o percentual de reajuste: "))

vlr_reajuste = reajuste * salario/100

novoSalario = salario + vlr_reajuste
print("O novo salário é de : R$", novoSalario)

print(f"O novo salário é de : R$ {novoSalario} ")