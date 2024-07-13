import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Estimativa de mortes por continente
dados = pd.read_csv("Dados Covid/covid_19.csv")

# continente = dados["continent"].fillna("outros").to_list()
# falecidos = dados["Deaths"].fillna(0).to_list()

# n_continente = continente[0:21]
# n_falecidos = falecidos[0:21]

# print(n_continente)
# print(n_falecidos)

# plt.title("Estimativa de mortes por continente")
# plt.bar(n_continente,n_falecidos)
# plt.show()

# Estimativa de recuperados por continente

recuperados = dados["Recovered"].fillna(0).to_list()
continente = dados["continent"].fillna("outros").to_list()

n_recuperados = recuperados[1:176]
n_continente = continente[1:176]

serie = pd.Series(n_continente,n_recuperados)

print(serie)
# print(n_continente)

plt.title("Estimativa de recuperados por continente")
plt.xlabel("Continentes")
plt.ylabel("Número de Recuperados")
plt.bar(n_continente,n_recuperados,color = "purple")
plt.grid(True)
plt.show()
