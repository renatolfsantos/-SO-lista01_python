# Declarando variáveis
n:int = 0
s:float = 1
f:int = 1

# Início
n = int(input("Digite o número para o cálculo da série 1 + 1/1! + 1/2! + ... + 1/N!: "))

for i in range(1, n + 1, 1):
    f *= i
    s += (1 / f)

print(f"O resultado da série é: {s}")
# Fim