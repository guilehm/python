# Tabuada em uma linha
# tabuada = [(a, b, a * b) for a in range(2, 3) for b in range(1, 11)]

# print(tabuada)
print("\n".join("{} x {} = {}".format(a, b, a * b) for a in range(1, 11) for b in range(1, 11)))
