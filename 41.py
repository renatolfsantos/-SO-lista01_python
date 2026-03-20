# Início
print("Todas as combinações possíveis entre dois dados que somados resultam em 7 são:")
for d1 in range(1, 7, 1):
    for d2 in range(1, 7, 1):
        if d1 + d2 == 7:
            print(d1, d2)
# Fim