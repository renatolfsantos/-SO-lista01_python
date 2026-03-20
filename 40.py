# Declarando variáveis
n1:int = 0
n2:int = 0
inicio:int = 0
fim:int = 0
primo:bool = False

# Início
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

inicio = min(n1, n2)
fim = max(n1, n2)

print(f"Os números primos entre {inicio} e {fim} são:")

for num in range(inicio + 1, fim, 1):
    if num >= 2:
        primo = True

        for i in range(2, int(num ** 0.5) + 1, 1):
            if num % i == 0:
                primo = False

        if primo:
            print(num)
# Fim