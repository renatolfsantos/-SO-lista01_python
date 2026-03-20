# Declarando variáveis
res:float = 1
isAdd:bool = False

# Início
for i in range (2 , 15, 1):
    if isAdd:
        res += i / (i * i)
    else:
        res -= i / (i * i)
    
    isAdd = not isAdd

print(f"O resultado da série 1 - 2/4 + 3/9 - 4/16 + 5/25 - ... + 15/225 é: {res}")
# Fim