# Declarando variáveis
ang1:float = 0
ang2:float = 0
ang3:float = 0

# Início
ang1 = float(input("Digite o valor do primeiro ângulo: "))
ang2 = float(input("Digite o valor do segundo ângulo: "))
ang3 = 180 - (ang1 + ang2)

print(f"O valor do terceiro ângulo será de {ang3:.2f} graus")
# Fim