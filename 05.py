# Declarando variáveis
a:int = 0
b:int = 0
c:int = 0
delta:float = 0
x1:float = 0
x2:float = 0

# Início
a = int(input("Digite o coeficiente A da equação: "))
b = int(input("Digite o coeficiente B da equação: "))
c = int(input("Digite o coeficiente C da equação: "))

delta = b ** 2 - 4 * a * c

x1 = (-b + delta**0.5) / (2 * a)
x2 = (-b - delta**0.5) / (2 * a)

print(f"As raízes da equação são aproximadamente: {x1:.2f} e {x2:.2f}")
# Fim