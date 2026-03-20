# Declarando variáveis
base:float = 0
exp:float = 0
res:float = 0

# Início
base = float(input("Digite a base: "))
exp = float(input("Digite o expoente: "))

res = base ** exp

print(f"{base} elevado a {exp} é: {res}")
# Fim