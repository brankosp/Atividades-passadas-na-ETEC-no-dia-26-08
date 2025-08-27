import random

numero_aleatorio = random.random()
print(numero_aleatorio)
print(50*"_")

numeroal = random.randrange(0,100)
print(numeroal)

print(50*"_")

numeroall = random.randrange(0,100,5)
print(numeroall)

print(50*"_")

lista = ["pao","leite","batata","proteina"]
print(random.choice(lista))

print(50*"_")

listas = ["pao","leite","batata","proteina"]
print(random.choices(listas,k=2))

