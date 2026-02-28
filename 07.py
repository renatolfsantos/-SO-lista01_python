# Declarando variáveis
comprimento:float = 0
largura:float = 0
altura:float = 0
volume:float = 0

# Início
comprimento = float(input("Digite o comprimento do paralelepípedo: "))
largura = float(input("Digite a largura do paralelepípedo: "))
altura = float(input("Digite a altura do paralelepípedo: "))

volume = comprimento * largura * altura

print(f"Seu volume é de aproximadamente: {volume:.2f}")
# Fim