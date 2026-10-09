prob_defeito = 0.01
prob_teste_positivo = 0.9
prob_falso_positivo = 0.05

prob_sem_defeito = 1 - prob_defeito

prob_teste = (prob_teste_positivo * prob_defeito) + (prob_falso_positivo * prob_sem_defeito)

prob_defeito_teste = (prob_teste_positivo * prob_defeito) / prob_teste

print(f"A probabilidade de o produto ser defeituoso, dado que o teste deu positivo, é de {prob_defeito_teste:.4f}")