# Declarando variáveis
salário: float = 0
novosalário: float = 0

# Início
salário = float(input("Digite o salário: "))

novosalário = salário * 1.15

print(f"O novo salário com o reajuste é: {novosalário:.2f}")
# Fim