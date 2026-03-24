dia = int(input("Digite a quantidade de dias:"))
horas = int(input("Digite a quantidade de horas:"))
minutos = int(input("Digite a quantidade de minutos:"))
segundos = int(input("Digite a quantidade de segundos:"))

total = segundos + minutos * 60 + horas * 60 * 60 + dia * 24 * 60 * 60
print("A quantidade de segundos é :", total)


dia = int(input("Digite a quantidade de dias:"))
horas = int(input("Digite a quantidade de horas:"))
minutos = int(input("Digite a quantidade de minutos:"))
segundos = int(input("Digite a quantidade de segundos:"))

# convertendo em segundos
segundos = segundos
minutos = minutos * 60
horas = horas * 60 * 60
dia = dia * 24 * 60 * 60
total =  dia + horas + minutos + segundos
print("A quantidade de segundos é :", total)