# Declarando variáveis
base: float = 0
altura: float = 0
área: float = 0

# Início
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

área = (base * altura) / 2

print(f"Sua área é de aproximadamente: {área:.2f}")
# Fim