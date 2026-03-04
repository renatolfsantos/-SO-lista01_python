# Declarando variáveis
nascimento:int = 0
atual:int = 0
idade:int = 0
futuro:int = 0

# Início
nascimento = int(input("Digite o ano de nascimento: "))
atual = int(input("Digite o ano atual: "))

idade = atual - nascimento
futuro = idade + 17

print("Sua idade atual é de", idade, "anos, daqui 17 anos ela será de", futuro, "anos")
# Fim