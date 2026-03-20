# Declarando variáveis
res:float = 1

# Início
for i in range (2, 51, 1):
    res += i / ((2 * i) + 1)

print(f"O resultado da série 1 + 2/3 + 3/5 + ... + 50/99 é: {res}")
# Fim