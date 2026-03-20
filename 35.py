# Declarando variáveis
n1:int = 0
n2:int = 0
soma:int = 0

# Início
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print(f"O maior número é: {n1}")
    for i in range (n2 + 1, n1, 1):
        if i % 2 != 0:
            soma += i
else:
    print(f"O maior número é: {n2}")
    for i in range (n1 + 1, n2, 1):
        if i % 2 != 0:
            soma += i

print(f"A soma dos valores ímpares entre os números é: {soma}")
# Fim