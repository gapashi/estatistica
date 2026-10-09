import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

media = 70
desvio_padrao = 10
n_alunos = 100

np.random.seed(42)
notas = np.random.normal(media, desvio_padrao, n_alunos)

plt.figure(figsize=(10, 6))
contagem, bins, ignored = plt.hist(notas, bins=15, density=True, alpha=0.6, color='blue', edgecolor='black')

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, media, desvio_padrao)
plt.plot(x, p, 'k', linewidth=2)

plt.title("Distribuição Normal das Notas dos Estudantes")
plt.xlabel("Notas")
plt.ylabel("Densidade de Probabilidade")
plt.grid(True)

plt.axvline(media, color='r', linestyle='dashed', linewidth=1)
plt.axvline(media - desvio_padrao, color='g', linestyle='dashed', linewidth=1)
plt.axvline(media + desvio_padrao, color='g', linestyle='dashed', linewidth=1)
plt.axvline(media - 2 * desvio_padrao, color='orange', linestyle='dashed', linewidth=1)
plt.axvline(media + 2 * desvio_padrao, color='orange', linestyle='dashed', linewidth=1)

plt.text(media, max(p) * 0.9, 'Média', color='red', ha='center', fontsize=12)
plt.show()