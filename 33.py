# Declarando variáveis
n:int = 0
f:float = 1

# Início
n = int(input("Digite o número para cálculo da série 1 + 1/2 + 1/3 + ... + 1/N: "))

for i in range (2, n + 1, 1):
    f += (1 / i)

print(f"A série terá como resultado: {f:.2f}")
# Fim