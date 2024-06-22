from calcular_media import calcular_media
from calcular_moda import calcular_moda
from calcular_mediana import calcular_mediana
from calcular_desvio_padrao import calcular_desvio_padrao
from calcular_variancia import calcular_variancia
from calcular_amplitude import calcular_amplitude

from matplotlib import pyplot as plt

alunos = {
    "Eduardo": {"Português": 10, "Matemática": 8, "História": 7, "Geografia": 7},
    "Kauã": {"Português": 8, "Matemática": 5, "História": 6, "Geografia": 7},
    "Samuel": {"Português": 6, "Matemática": 5, "História": 2, "Geografia": 9},
}

# Extrair nomes dos alunos e notas de cada aluno
nomes_alunos = list(alunos.keys())
notas_portugues = [alunos[aluno]["Português"] for aluno in nomes_alunos]
notas_matematica = [alunos[aluno]["Matemática"] for aluno in nomes_alunos]
notas_historia = [alunos[aluno]["História"] for aluno in nomes_alunos]
notas_geografia = [alunos[aluno]["Geografia"] for aluno in nomes_alunos]

# Configurar os dados para plotagem
materias = ["Português", "Matemática", "História", "Geografia"]
notas = [notas_portugues, notas_matematica, notas_historia, notas_geografia]
cores = ['b', 'g', 'r', 'c']  # Cores para cada matéria

# Plotar gráfico
plt.figure(figsize=(10, 6))  # Tamanho da figura

for i in range(len(materias)):
    plt.bar(nomes_alunos, notas[i], color=cores[i], alpha=0.6, label=materias[i])

plt.title("Notas dos Alunos por Matéria")
plt.xlabel("Alunos")
plt.ylabel("Notas")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotacionar os nomes dos alunos para melhor visualização

plt.tight_layout()
plt.show()

