#to começando

import random


char_hp = 100
foe_hp = 100
att_stat = 15






def command_list():
    comandos = ['dice', 'combat']
    print('Comandos válidos:', comandos)


def dice():
    D6 = list(range(1, 7))
    D20 = list(range(1, 21))
    D100 = list(range(1, 101))
    D4 = list(range(1, 5))
    dado_type = input('Qual dado vc quer rolar? (D4, D6, D20, D100) ')
    dado_rep = int(input('Quantas vezes? '))
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

def combat_dice(damage):
    D6 = list(range(1, 7))
    D20 = list(range(1, 21))
    D100 = list(range(1, 101))
    D4 = list(range(1, 5))
    dado_type = input('Qual dado vc quer rolar? (D4, D6, D20, D100) ')
    dado_rep = int(input('Quantas vezes? '))
    while dado_rep > 0:
        if dado_type == 'd6' or dado_type == 'D6':
            dado_roll = random.choice(D6)
            print('Você rolou o número', dado_roll)
            damage.append(dado_roll)
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


def combat(char_hp, foe_hp, att_stat):
    damage = []
    while char_hp > 0 and foe_hp > 0:
        action = input('O que você vai fazer? (fight, run)').lower()
        if action == 'fight':
            combat_dice(damage)
            print(damage)

def functions(choice):
    if choice == 'dice':
        dice()
    if choice == 'command_list':
        command_list()
    if choice == 'combat':
        combat(char_hp, foe_hp, att_stat)
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
