#Esse programa tem a finalidade de pegar um angulo qualquer e mostrar o seno,cosseno ea tangente  
#Autor : Kaique Sousa
#Data : 26/08/2025

import math# Importa a bliblioteca 

angulo = float(input("Digite o angulo desejado :"))#Recebe o angulo
radios = math.radians(angulo)#converte para radios 

seno = math.sin(radios)#Calcula o seno
coseno = math.cos(radios)#Calcula o  cosseno
tangente = math.tan(radios)#Calcula a tangente

print(f"O seno é :{seno}")#Mostra o resultado 
print(f"O cosseno é:{coseno}")#Mostra o resultado
print(f"A tangente é:0{tangente}")#Mostra o resultado