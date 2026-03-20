# Declarando variáveis
n:int = 0

# Início
n = int(input("Digite o número para cálculo da tabuada: "))

print(f"A tabuada do {n} é: ")
for i in range (1, 11, 1):
    print(n * i)
# Fim