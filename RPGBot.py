#to começando
import random

def dice():
    D6 = list(range(1, 7))
    D20 = list(range(1, 21))
    D100 = list(range(1, 101))
    D4 = list(range(1, 5))


    def dice_rolling(dado_type, dado_rep):
        while dado_rep > 0:
            if dado_type == 'd6' or dado_type == 'D6':
                dado_roll = random.choice(D6)
                print('Você rolou o número', dado_roll)
                dado_rep = dado_rep - 1
            if dado_type == 'd20' or dado_type == 'D20':
                dado_roll = random.choice(D20)
                print('Você rolou o número', dado_roll)
                dado_rep = dado_rep - 1
            if dado_type == 'd100' or dado_type == 'D100':
                dado_roll = random.choice(D100)
                print('Você rolou o número', dado_roll)
                dado_rep = dado_rep - 1
            if dado_type == 'd4' or dado_type == 'D4':
                dado_roll = random.choice(D4)
                print('Você rolou o número', dado_roll)
                dado_rep = dado_rep - 1
        if dado_rep == 0:
            print('Pronto!')



    dice_rolling(input('Qual dado você quer rolar? (D6, D20) '), int(input('Quantas vezes?')))
dice()
