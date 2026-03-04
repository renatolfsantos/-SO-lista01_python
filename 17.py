# Declarando variáveis
litros:float = 0
percurso:float = 0
velmedia: float = 0

# Início
percurso = float(input("Digite o tempo de percurso: "))
velmedia = float(input("Digite a velocidade média do automóvel: "))

litros = (percurso * velmedia) / 12

print(f"Serão gastos {litros:.2f} litros")
# Fim