# main.py

from calculo_media import calcular_media
from calculo_moda import calcular_moda
from calculo_variancia import calcular_variancia
from calculo_desvio_padrao import calcular_desvio_padrao
from encontrar_menor_nota import encontrar_menor_nota
from encontrar_maior_nota import encontrar_maior_nota

def calcular_estatisticas_notas(notas):
    media = calcular_media(notas)
    moda = calcular_moda(notas)
    variancia = calcular_variancia(notas)
    desvio_padrao = calcular_desvio_padrao(notas)
    menor_nota = encontrar_menor_nota(notas)
    maior_nota = encontrar_maior_nota(notas)
    
    return media, moda, variancia, desvio_padrao, menor_nota, maior_nota

# Exemplo de uso
if __name__ == "__main__":
    notas_alunos = [7.5, 8.2, 6.9, 7.5, 8.0, 7.5, 7.0, 8.5]
    media, moda, variancia, desvio_padrao, menor_nota, maior_nota = calcular_estatisticas_notas(notas_alunos)
    
    print("Estatísticas das notas dos alunos:")
    print(f"Média: {media}")
    print(f"Moda: {moda}")
    print(f"Variância: {variancia}")
    print(f"Desvio padrão: {desvio_padrao}")
    print(f"Menor nota: {menor_nota}")
    print(f"Maior nota: {maior_nota}")

