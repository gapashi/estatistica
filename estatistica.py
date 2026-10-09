import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# idades = np.random.randint(18, 50, size=10)
# print(idades)

valores = [10, 10, 2, 6, 15, 20, 19, 5] # 2, 5, 6, 10, 10, 15, 19, 20
print(valores)

somatoria = np.sum(valores)
print(f"Soma de todos os números da lista aleatória: {somatoria}")

media = np.mean(valores)
print(f"Média de todos os valores da lista aleatória: {media}")

valores.sort()
mediana = np.median(valores)
print(f"A mediana da lista aleatória é: {mediana}")

moda = stats.mode(valores, keepdims=False)
moda_valor = moda.mode
print(f"A moda da lista aleatória é: {moda_valor}")

# VARIANCIA
variancia = np.var(valores)
print(variancia)

# DESVIO PADRAO
desvio_padrao = np.std(valores)
print(desvio_padrao)

# AMPLITUDE
amplitude = np.ptp(valores)
print(f"Amplitude: {amplitude}")