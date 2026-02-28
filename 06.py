# Declarando variáveis
x:float = 0
y:float = 0
t:float = 0

# Início
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

t = x
x = y
y = t

print(f"Com os valores trocados, x = {x} e y = {y}")
# Fim