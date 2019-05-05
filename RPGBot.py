#começa a ler de baixo pra cima (while, functions, combat, combat_dice, dice, command_list), vai ser mais fácil de entender

import random
import pickle

char_hp = 100
foe_hp = 100
att_stat = 50

def force_start():
    char_list = [' ']
    with open('char_doc.txt', 'wb') as fp:
        pickle.dump(char_list, fp)
    print('Save iniciado!')

def load():
    fp = open('char_doc.txt', 'rb')
    char_list = pickle.load(fp)
    print(char_list)

def save():
    with open ('char_doc.txt', 'rb') as fp:
        itemlist = pickle.load(fp)
        print(itemlist)

def desenho():
    print(':-)')

def command_list(): #lista dos comandos possíveis no começo do programa
    comandos = ['dice', 'combat', 'characters']
    print('Comandos válidos:', comandos)

def create_char(char_list):
    char_hp = 0
    char_att = 100
    char_luck = 100
    char_class = 0
    char_name = input('Nome do personagem: ')
    race = input('Qual a raça do personagem? (Humano, Elfo, Anão) ')
    if race.lower() == 'elfo':
        char_hp = 75
    if race.lower() == 'humano':
        char_hp = 100
    if race.lower() == 'anão':
        char_hp = 125
    classe = input('Qual a classe do seu personagem? (Mago, DPS, Guerreiro) ')
    if classe.lower() == 'mago':
        char_hp = char_hp * 0.9
        char_att = char_att * 1.5
        char_luck = char_luck * 0.5
    if classe.lower() == 'dps':
        char_hp = char_hp * 0.75
        char_att = char_att * 1.2
        char_luck = char_luck * 0.85
    if classe.lower() == 'guerreiro':
        char_hp = char_hp * 1.5
        char_att = char_att * 1
        char_luck = char_luck * 0.75
    backstory = input('Qual a backstory do seu personagem? ')
    char_name = [char_name, char_hp, char_att, char_luck, backstory]
    char_list.append(char_name) #TEXTANDO PICKLE COMO SISTEMA DE SALVAMENTO
    with open('char_doc.txt', 'wb') as fp:
        pickle.dump(char_list, fp)
    print('Personagem criado!')
    print('Nome:', char_name[0])
    print('HP:', char_name[1])
    print('Ataque:', char_name[2])
    print('Backstory:', char_name[4])

def characters():
    choice = input('Selecione uma opção: (create, view, stats)')
    if choice.lower() == 'create':
        create_char(char_list)
    if choice.lower() == 'view':
        print(char_list)
    if choice.lower() == 'stats':
        print(char_list)
        char_select = input('De qual personagem? (1, 2, 3...) ')
        char_select = char_list[int(char_select)]
        print('Nome:', char_select[0])
        print('HP:', char_select[1])
        print('Ataque:', char_select[2])
        print('Backstory:', char_select[4])

def dice(): #joga os dados, mostra os resultados.
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
    dado_rep = int(input('Quantas vezes? ')) #define o contador (vezes que vai jogar o dado)
    while dado_rep == 0: #loop caso o usuário escolha 0, ele precisa escolher alguem número diferente de 0
        print('Escolha quantas vezes rolar o dado! ')
        dado_rep = int(input('Quantas vezes? '))
    while dado_rep > 0: #enquanto o contador for > 0, o loop continua
        if dado_type == 'd6' or dado_type == 'D6':
            dado_roll = random.choice(D6)
            print('Você rolou o número', dado_roll)
            damage.append(dado_roll) #coloca o valor dos dados na lista 'damage'
            dado_rep = dado_rep - 1 #diminui o contador
        if dado_type == 'd20' or dado_type == 'D20':
            dado_roll = random.choice(D20)
            print('Você rolou o número', dado_roll)
            damage.append(dado_roll)
            dado_rep = dado_rep - 1
        if dado_type == 'd100' or dado_type == 'D100':
            dado_roll = random.choice(D100)
            print('Você rolou o número', dado_roll)
            damage.append(dado_roll)
            dado_rep = dado_rep - 1
        if dado_type == 'd4' or dado_type == 'D4':
            dado_roll = random.choice(D4)
            print('Você rolou o número', dado_roll)
            damage.append(dado_roll)
            dado_rep = dado_rep - 1
    if dado_rep == 0: #quando o contador zera, o processo para
        print('...')

def combat(char_hp, foe_hp, att_stat): #MODO DE COMBATE
    damage = [] #INICIA A LISTA DE DANO
    while char_hp > 0 and foe_hp > 0:
        action = input('O que você vai fazer? (fight, run) ').lower()
        if action == 'fight':
            combat_dice(damage) #chama a função dos dados de combate
            for i in damage: #pega o resultado dos dados e passa pelo loop
                if i == damage[0]: #pro primeiro item da lista não acontece nada, pode acontecer de bugar o código com números repetidos
                    print('CALCULANDO DANO...')
                else: #pros outros itens, eles são somados ao primeiro
                    damage[0] = damage[0] + i
            print('O dano causado foi', damage[0]) #mostra o primeiro valor
            foe_hp = foe_hp - damage[0] #subtrai da vida do inimigo o dano causado
            damage = [] #esvazia a lista de dano, dessa forma dá pra repetir o processo quanto precisar
        if action == 'run': #se escolher 'run' vai rolar 2 dados, se a média entre eles for > 2.5 vc foge, se não for vc fica
            run_dice = list(range(1, 7))
            chance = random.choice(run_dice) + random.choice(run_dice)
            chance = chance/2
            if chance > 2.5:
                print('Você fugiu!')
                break
            else:
                print('Não conseguiu fugir!!!')
    if char_hp <= 0: #se vc morrer vc morre (ainda não tem como vc levar dano, mas vai ter)
        print('VOCÊ MORREU...') #git gud
    if foe_hp <= 0: #se o maluco morrer vc ganha
        print('VOCÊ VENCEU!!!')

def functions(choice): #função que chama as outras
    if choice == 'dice':
        dice()
    if choice == 'command_list':
        command_list()
    if choice == 'combat':
        combat(char_hp, foe_hp, att_stat)
    if choice == 'characters':
        characters()
    if choice == 'desenho':
        desenho()
    if choice == 'exit':
        um_mais_um = 2
    if choice == 'save':
        save()
    if choice == 'load':
        load()
    if choice == 'force_start':
        force_start()
    else:
        while True:
            print('Pra acessar a lista de comandos, entre com command_list')
            functions(input('Entre com um comando: ').lower())

while True: #loop da UI, vc escolhe se vai continuar no loop ou terminar o programa
    loop = input('Inserir comando? (y/n) ').lower()
    if loop == 'y':
        functions(input('Entre com um comando: ').lower())
    if loop == 'n':
        print('Fim do processo')
        break
    else:
        print('...')
