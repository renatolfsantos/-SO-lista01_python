# Declarando variáveis
horas:int = 0
valor:float = 0
desconto:float = 0
descendentes:int = 0
salario:float = 0

# Início
horas = int(input("Digite o total de horas trabalhadas: "))
valor = float(input("Digite o valor por hora: "))
desconto = float(input("Digite o desconto: "))
descendentes = int(input("Digite o número de descendentes: "))

salario = ((horas * valor) - desconto) + 100 * descendentes

print(f"O salário a receber será: {salario:.2f}")
# Fim