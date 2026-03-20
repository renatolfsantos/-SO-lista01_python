import math

# Declarando variáveis
a:float = 0
b:float = 0
c:float = 0
x1:float = 0
x2:float = 0
delta:float = 0

# Início
a = float(input("Digite o valor do coeficiente A: "))
b = float(input("Digite o valor do coeficiente B: "))
c = float(input("Digite o valor do coeficiente C: "))

delta = (b * b) - (4 * a * c)

if delta < 0:
    print("Não há soluções reais para a equação")
else:
    x1 = -b + math.sqrt(delta)
    x2 = -b - math.sqrt(delta)
    print(f"As raízes da função são: {x1:.2f} e {x2:.2f}")

# Fim