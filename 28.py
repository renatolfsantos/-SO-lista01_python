# Declarando variáveis
p: float = 0
m: int = 0
np: float = 0

# Início
p = float(input("Digite o preço atual: "))
m = int(input("Digite a média mensal de vendas: "))

np = p

if m < 500 and p < 30:
    np *= 1.1
elif m < 1000 and p < 80:
    np *= 1.15
else:
    np *= 0.95

print(f"O novo preço será: {np:.2f} reais")
# Fim