# Declarando variáveis
n:int = 0
f:int = 1

# Início
n = int(input("Digite o número para cálculo do fatorial: "))

for i in range (2, n + 1, 1):
    f *= i

print(f"O fatorial de {n} é: {f}")
# Fim