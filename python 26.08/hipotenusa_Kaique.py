# Esse programa tem a inteção de ler o comprimeto do cateto oposto e adjacentes de um triangulo retangulo e calcule o comprimento da hipotenusa
# Autor: Kaique Sousa
# Data: 26/08/20025

import math # Importa a bliblioteca 

cateto_oposto = float(input("Digite o comprimento do cateto :"))#Salva o primeiro valor do cateto
cateto_adjacente = float(input("Digite o comprimento do cateto :"))#Salva o segundo valor 

hipotenusa = math.hypot(cateto_oposto , cateto_adjacente)#faz o calculo entre a primeira e segunda variavel 

print(f"o Valor da hipotenusa é :{hipotenusa}")# mostra o resultado 