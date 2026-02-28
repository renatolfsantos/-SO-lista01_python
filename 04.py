# Declarando variáveis
celsius: float = 0
fahrenheit: float = 0

# Início
celsius = int(input("Sua temperatura em Celsius é: "))

fahrenheit = (celsius * 9 + 160) / 5

print(f"Sua temperatura em Fahrenheits é de aproximadamente: {fahrenheit:.2f}")
# Fim