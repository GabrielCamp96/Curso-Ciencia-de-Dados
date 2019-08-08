# moeda dar cara 3 vezes em 5 lançamentos

dbinom(3, 5, 0.5)

# 4 sinais 4 tempos, prob = 0, 1, 2, 3, 4 sinais verdes

dbinom(0, 4, 0.25)
dbinom(1, 4, 0.25)
dbinom(2, 4, 0.25)
dbinom(3, 4, 0.25)
dbinom(4, 4, 0.25)
pbinom(2, 4, 0.25) # soma das probabilidades até 2

# prova 12 questões

# 7 questões, 4 alternativas

dbinom(7, 12, 0.25)