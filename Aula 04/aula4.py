import statistics

dados = list(range(100,600))
varianca = statistics.variance(dados)
print(f"{varianca:.2f}")

dados = list(range(100,1000,2))
