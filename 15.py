import math

# Declarando variáveis
cat1:float = 0
cat2:float = 0
hip:float = 0

# Início
cat1 = float(input("Digite o valor do primeiro cateto: "))
cat2 = float(input("Digite o valor do segundo cateto: "))

hip = math.sqrt(cat1**2 + cat2 **2)

print(f"A hipotenusa será: {hip:.2f}")
# Fim