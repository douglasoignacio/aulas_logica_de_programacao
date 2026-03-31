preço = float(input("Digite o valor do litro de Gasolina: R$ "))
desempenho = float(input("Digite o consumo em Km/L de seu veículo: "))
distancia = int(input("Digite a distância que irá percorrer até a proxima cidade: "))

litros = distancia / desempenho
valor = litros * preço

print("Sua viagem custará R$", valor,", e gastará ",litros," de gasolina.")

print(f"Sua viagem custará R$ {valor}, e gastará {litros} de gasolina.")