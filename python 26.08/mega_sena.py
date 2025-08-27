#Esse programa tem a função de sorteia 6 numeros de 1 á 60 
#Autor:  Kaique Sousa
#Data : 26/08/2025
 
import random

# A função random.sample() é perfeita para isso.
# O primeiro argumento é a sequência de onde sortear (range(1, 61)).
# O segundo argumento é a quantidade de números que você quer sortear (6).
numeros_sorteados = random.sample(range(1, 61), 6)

# Ordena os números em ordem crescente (opcional, mas comum em jogos de loteria)
numeros_sorteados.sort()

print("Os 6 números sorteados de 1 a 60 são:")
print(numeros_sorteados)