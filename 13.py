# Declarando variáveis
alimento:float = 0
dias:int = 0

# Início
alimento = float(input("Digite a quantidade, em kg, de alimento: "))

dias = int((alimento * 1000) // 50)

print("A quantidade fornecida durará por", dias, "dias")
# Fim