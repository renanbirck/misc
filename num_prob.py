#!/usr/bin/python3

from random import randint
num_randoms = 10000     # Quantidade de numeros aleatorios a gerar

random_numbers = [randint(1, 5) for _ in range(num_randoms)]  # Vetor aleatorio

count_4 = len([x for x in random_numbers if x==4])  # Filtrar quantos '4' e contar

print("Total de 4: {} ({}%)".format(count_4, 100*count_4/num_randoms) )
