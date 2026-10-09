import random
import matplotlib.pyplot as plt

# def lancar_dado(numero_lancamentos):
#     ocorrencias = 0
#     for _ in range(numero_lancamentos):
#         if random.randint(1, 6) == 3:
#             ocorrencias += 1
#         return ocorrencias / numero_lancamentos
#         #random.uniform(0, 1) < 0.5:

# for lancamentos in [10, 100, 1000, 10000, 100000]:
#     probabilidade_estimada = lancar_dado(lancamentos)
#     print(f"Número de lançamentos: {lancamentos} / Frequência relativa do número 3: {probabilidade_estimada:.4f}")

def simular_lancamentos(n):
    cara = 0
    prob_caras = []

    for i in range(1, n+1):
        resultado = random.choice(['cara', 'coroa'])
        if resultado == 'cara':
            cara += 1

        iesimo = cara/i
        prob_caras.append(iesimo)
    return prob_caras

n = 1000
#simular_lancamentos(1000)

prob_caras = simular_lancamentos(n)

plt.figure(figsize=(10, 6))
plt.plot(prob_caras, label='Probabilidade de "cara"')
plt.axhline(y=0.5, color='r', linestyle='--', label='Valor de Probabilidade Esperado')

plt.xlabel('Número de Lançamentos')
plt.ylabel('Probabilidades')
plt.title('Probabilidade de sair Cara')

plt.legend()
plt.grid(True)

plt.show()