# Declarando variáveis
depósito: float = 0
poupança: float = 0

# Início
depósito = float(input("Digite o valor depositado: "))

poupança = depósito * 1.013

print(f"Após 1 mês, o valor na poupança será: {poupança:.2f}")
# Fim