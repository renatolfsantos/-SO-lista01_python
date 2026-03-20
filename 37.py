# Declarando variáveis
n:int = 0
a:int = 0
b:int = 1

# Início
n = int(input("Digite o enésimo número da sequência de fibonacci: "))

for i in range(0, n, 1):
    print(a, end= " ")
    a, b = b, a + b
# Fim