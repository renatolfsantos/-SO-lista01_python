# Declarando variáveis
tipo:int = 0
valor:float = 0

# Início
tipo = int(input("Digite o tipo de investimento: "))
valor = float(input("Digite o valor do investimento: "))

if tipo == 1:
    valor *= 1.03
    print(f"Após 30 dias, o valor corrigido será: {valor:.2f}")
elif tipo == 2:
    valor *= 1.05
    print(f"Após 30 dias, o valor corrigido será: {valor:.2f}")
else:
    print("Tipo de investimento desconhecido")
# Fim