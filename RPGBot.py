#to começando
import random

D6 = [1, 2, 3, 4, 5, 6]
D20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def dado(dado_type, dado_rep):
    while dado_rep > 0:
        if dado_type == 'd6' or dado_type == 'D6':
            dado_roll = random.choice(D6)
            print('Você rolou o número', dado_roll)
            dado_rep = dado_rep - 1
        if dado_type == 'd20' or dado_type == 'D20':
            dado_roll = random.choice(D20)
            print('Você rolou o número', dado_roll)
            dado_rep = dado_rep - 1
    if dado_rep == 0:
        print('Pronto!')



dado(input('Qual dado você quer rolar?'), int(input('Quantas vezes?')))
