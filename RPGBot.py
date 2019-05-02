#to começando

import random

def command_list():
    comandos = ['dice']
    print('Comandos válidos:', comandos)

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

def functions(choice):
    if choice == 'dice':
        dice()
    if choice == 'command_list':
        command_list()
    else:
        print('Pra acessar a lista de comandos, entre com command_list')

while True:
    loop = input('Inserir comando? (y/n) ').lower()
    if loop == 'y':
        functions(input('Entre com um comando: ').lower())
    if loop == 'n':
        print('Fim do processo')
        break
    else:
        print('Por favor, entre com uma resposta válida')
