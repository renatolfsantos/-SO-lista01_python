import math

# Declarando variáveis
raio:float = 0
comprimento:float = 0

# Início
raio = float(input("Digite o raio da circunferência: "))

comprimento = 2 * raio * math.pi

print(f"O comprimento da circunferência é de aproximadamente: {comprimento:.2f}")
# Fim