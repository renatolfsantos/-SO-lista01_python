# Declarando variáveis
v: int = 0
s: float = 0
t: int = 0
vm: float = 0

# Início
v = int(input("Digite o número de voltas: "))
s = float(input("Digite a extensão do circuito em metros: "))
t = int(input("Digite o tempo de duração em minutos: "))

s *= v / 1000

vm = s / (t / 60)

print(f"A velocidade média foi de {vm:.2f} km/h")
# Fim