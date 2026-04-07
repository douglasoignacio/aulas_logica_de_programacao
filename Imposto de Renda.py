print("\nSIMULAÇÃO PARA CÁLCULO DE IMPOSTO DE RENDA DE PESSOA FÍSICA EXERCÍCIO 2026/ANO CALENDÁRIO 2025:\n")
# Coletar dado do rendimento
rendMensal = float(input("INFORME SEUS RENDIMENTOS MENSAIS TRIBUTÁVEIS: \nR$ "))
# Usuário decide informação de entrada entre Deduções Legais ou Desconto Simplificado
print("\nINFORME A OPÇÃO PELA TRIBUTAÇÃO PARA CÁLCULO DO IMPOSTO DE RENDA:")
escolha = int(input("DIGITE (1) PARA DEDUÇÕES LEGAIS \n       (2) PARA DESCONTO SIMPLIFICADO (25%):\nDIGITE A OPÇÃO: "))

if escolha == 1:

    # Calculo do Imposto de Renda Simplificado
    # Tabela Progressiva Mensal do Imposto de Renda em 2026
    # Base de Cálculo                   Aliquota        Deduções
    # Até R$ 2.428,80                   Isento          -
    # De R$ 2.428,81 a R$ 2.826,65      7,5%            R$ 182,16
    # De R$ 2.826,65 a R$ 3.751,05      15%             R$ 394,16
    # De R$ 3.751,05 a R$ 4.664,68      22,5%           R$ 675,49
    # Acima de R$ 4.664,68              27,5%           R$ 908,73

    # Índices das tabelas para cálculo do IR
    faixa = [2428.8, 2826.65, 3751.05, 4664.68]
    deducao = [182.16, 394.16, 675.49, 908.73]
    aliquota = [0.075, 0.15, 0.225, 0.275]

    if  rendMensal <= faixa[0]:
        # Calculo para rendimento inferiores a R$ 2.428,80
        ImpRend = 0 # Rendimento Isento, imposto a pagar = 0
        alqUtil = 0 # Rendimento Isento, aliquota = 0

    elif    rendMensal <= faixa[1]:
        # Calculo para rendimento entre R$ 2.428,81 e R$ 2.826,65
        ImpRend = (rendMensal * aliquota[0]) - deducao[0]
        alqUtil =  aliquota[0] * 100

    elif    rendMensal <= faixa[2]:
        # Calculo para rendimento entre R$ 2.826,66 e R$ 3.751,05
        ImpRend = (rendMensal * aliquota[1]) - deducao[1] 
        alqUtil =  aliquota[1] * 100

    elif    rendMensal <= faixa[3]:
        # Calculo para rendimento entre R$ 3.751,05 e R$ 4.664,68
        ImpRend = (rendMensal * aliquota[2]) - deducao[2]
        alqUtil =  aliquota[2] * 100

    else: 
        # Calculo para rendimentos superiores a R$ 4.664,68
        ImpRend = (rendMensal * aliquota[3]) - deducao[3]
        alqUtil =  aliquota[3] * 100

    if ImpRend > 0:
        ImpRend = ImpRend
    else:
        ImpRend = 0

    # Usuário informa sobre deduções para abatimento
    print("\nINFORME SE POSSUI DEPENDENTES: (VALOR ANUAL A DEDUZIR POR DEPENDENTE DE R$ 2.275,08)")
    escolha = int(input("DIGITE (1) PARA SIM \n       (2) PARA NÃO:\nDIGITE A OPÇÃO: "))

    # Dedução Máxima Anual por dependente R$ 2.275,08 (Limite Mensal R$ 189,59)
    limDep = 2275.08
    if escolha == 1:
        quantDepend = int(input("INFORME A QUANTIDADE DE DEPENDENTES: (LIMITE MÁXIMO MENSAL DE R$ 189,59)\n"))
        dependente = quantDepend * limDep / 12

    elif escolha == 2:
        dependente = 0

    else:
        dependente = 0

    # Dedução |Máxima Anual por dependente R$ 3.561,50 (Limite Mensal R$ 296,79)
    print("\n DESEJA DECLARAR DESPESAS COM INSTRUÇÃO? (VALOR MÁXIMO ANUAL A DEDUZIR DE R$ 3.561,50)")
    limInst = 3561.50
    escolha1 = int(input("DIGITE (1) PARA SIM \n       (2) PARA NÃO:\nDIGITE A OPÇÃO: "))

    if escolha1 == 1:
        instrucao = float(input("INFORME O VALOR GASTO COM INSTRUÇÃO: (LIMITE MÁXIMO MENSAL DE R$ 296,79)\n" ))
        if instrucao < limInst:
            instrucao = instrucao / 12

        else:
            instrucao = limInst / 12

    elif escolha1 == 2:
        instrucao = 0

    else:
        instrucao = 0
              
    Deducao = dependente + instrucao
    ImpDed = ImpRend - Deducao

    if ImpDed > 0:
        ImpDed = ImpDed
    else:
        ImpDed = 0

    print(f"PARA O RENDIMENTO MENSAL BRUTO DE R$: { rendMensal:.2f}")
    print(f"A BASE DE CÁLCULO DO IMPOSTO É DE R$: {rendMensal:.2f} E A ALIQUOTA UTILIZADA FOI DE {alqUtil:.0f} %")
    print(f"O VALOR MENSAL DEVIDO DE IMPOSTO DE RENDA A PAGAR COM AS DEDUÇÕES LEGAIS É DE R$ {ImpDed:.2f}")
    print(f"SEU SALÁRIO LÍQUIDO PARA O PERIODO FOI DE R$ {rendMensal - ImpDed:.2f}")    
    if ImpDed == 0:
        print("RENDIMENTO ISENTO DE IMPOSTO DE RENDA!")

elif escolha == 2:

    # O calculo do valor é definido como 25% do limite máximo da faixa de alíquota zero (isenta) R$ 2.428,80   
    RendSimp = rendMensal - rendMensal * .25

    # Calculo do Imposto de Renda Simplificado
    # Tabela Progressiva Mensal do Imposto de Renda em 2026
    # Base de Cálculo                   Aliquota        Deduções
    # Até R$ 2.428,80                   Isento          -
    # De R$ 2.428,81 a R$ 2.826,65      7,5%            R$ 182,16
    # De R$ 2.826,65 a R$ 3.751,05      15%             R$ 394,16
    # De R$ 3.751,05 a R$ 4.664,68      22,5%           R$ 675,49
    # Acima de R$ 4.664,68              27,5%           R$ 908,73

    # Índices das tabelas para cálculo do IR
    faixa = [2428.8, 2826.65, 3751.05, 4664.68]
    deducao = [182.16, 394.16, 675.49, 908.73]
    aliquota = [0.075, 0.15, 0.225, 0.275]

    if  RendSimp <= faixa[0]:
        # Calculo para rendimento inferiores a R$ 2.428,80
        ImpRend = 0 # Rendimento Isento, imposto a pagar = 0
        alqUtil = 0 # Rendimento Isento, aliquota = 0

    elif    RendSimp <= faixa[1]:
        # Calculo para rendimento entre R$ 2.428,80 e R$ 2.826,65
        ImpRend = (RendSimp * aliquota[0]) - deducao[0]
        alqUtil =  aliquota[0] * 100

    elif    RendSimp <= faixa[2]:
        # Calculo para rendimento entre R$ 2.826,65 e R$ 3.751,05
        ImpRend = (RendSimp * aliquota[1]) - deducao[1]
        alqUtil =  aliquota[1] * 100

    elif    RendSimp <= faixa[3]:
        # Calculo para rendimento entre R$ 3.751,05 e R$ 4.664,68
        ImpRend = (RendSimp * aliquota[2]) - deducao[2]
        alqUtil =  aliquota[2] * 100

    else: 
        # Calculo para rendimentos superiores a R$ 4.664,68 (faixa4)
        ImpRend = (RendSimp * aliquota[3]) - deducao[3]
        alqUtil =  aliquota[3] * 100

    # Limite Mensal de Desconto Simplificado R$ 607,20
    if ImpRend > 0:
        ImpRend = ImpRend
    else:
        ImpRend = 0

    print("PARA O RENDIMENTO MENSAL BRUTO DE R$:", rendMensal,)
    print("A BASE DE CÁLCULO DO IMPOSTO É DE R$:", RendSimp, "E A ALIQUOTA UTILIZADA FOI DE", alqUtil,"%")
    print("O VALOR MENSAL DEVIDO DE IMPOSTO DE RENDA A PAGAR COM AS DEDUÇÕES LEGAIS É DE R$ ",ImpRend)
    print("SEU SALÁRIO LÍQUIDO PARA O PERIODO FOI DE R$", rendMensal - ImpRend)    
    if ImpRend == 0:
        print("RENDIMENTO ISENTO DE IMPOSTO DE RENDA!")

else:
    # Mensagem de retorno de erro
    print("Valor Inválido!")
    escolha = 0
