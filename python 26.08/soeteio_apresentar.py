#Esse programa tem a finalidade de sortea a ordem de apresentação de trabalho dos alunos  
#Autor : Kaique Sousa
#Data : 26/08/2025
import random

# Lista dos nomes dos alunos
alunos = ["Kaique", "Kauê", "Henrique", "Miguel"]

# Embaralha a lista em uma ordem aleatória
random.shuffle(alunos)

# Imprime a nova ordem de apresentação
print("A ordem de apresentação dos trabalhos é:")
for i, aluno in enumerate(alunos):
    print(f"{i + 1}. {aluno}")