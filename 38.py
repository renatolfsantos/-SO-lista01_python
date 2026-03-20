# Declarando variáveis
ma: int = 0
me: int = 0
n: int = 0

# Início
for i in range(1, 101, 1):
    n = int(input(f"Digite o {i}º número: "))

    if i == 1:
         ma = n
         me = n
    else:
        if n > ma:
            ma = n
        if n < me:
                me = n

print(f"O maior número é: {ma}")
print(f"O menor número é: {me}")
# Fim