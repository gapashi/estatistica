sensibilidade = 0.95
especificidade = 0.98
infectados = 0.02

p_nao_infectados = 1 - infectados
p_falso_positivo = 1 - especificidade

p_positivo = (sensibilidade * infectados) + (p_falso_positivo * p_nao_infectados)

p_infectado_positivo = (sensibilidade * infectados) / p_positivo

print(f"Probabilidade de a pessoa estar realmente infectada, dado que o teste deu positivo, é de: {p_infectado_positivo * 100:.2f}%")