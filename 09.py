# Declarando variáveis
x:int = 0
y:int = 0
soma:int = 0
# Início
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

soma = x * x + y * y

print(f"A soma dos quadrados dos números em questão é: {soma:.2f}")
# Fim