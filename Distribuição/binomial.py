from scipy.stats import binom

# Jogar uma moeda 5 vezes, qual a probabilidade de dar cara 3 vezes?

prob = binom.pmf(3, 5, 0.5)
print("Moeda: %f" % prob)

# Passar por 4 sinais de 4 tempos, qual a probabilidade de pegar sinal verde
# nenhuma, 1, 2, 3 ou 4 vezes seguidas?
print("Nenhuma: %f" % binom.pmf(0, 4, 0.25))
print("Um sinal: %f" % binom.pmf(1, 4, 0.25))
print("Dois sinais: %f" % binom.pmf(2, 4, 0.25))
print("Três sinais: %f" % binom.pmf(3, 4, 0.25))
print("Quatro sinais: %f" % binom.pmf(4, 4, 0.25))

# Probabilidade acumulativa
print("Acumulativa para 2 sinais verdes: %f" % binom.cdf(2,4,0.25))

# Concurso de 12 questões, qual a probabilidade de acertar 7 questões considerando
# que cada questão tem 4 alternativas.
print("Probabilidade de 7 questões corretas: %f " % binom.pmf(7, 12, 0.25))