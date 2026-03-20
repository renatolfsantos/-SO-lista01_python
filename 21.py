# Declarando variáveis
n1:float = 0
n2:float = 0
n3:float = 0
n4:float = 0
media:float = 0

# Início
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3= float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4

if media >= 6:
    print("APROVADO")
elif media >= 3:
    print("EXAME")
else:
    print("RETIDO")
# Fim