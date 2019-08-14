#Os personagens, classes, raças, etc são objetos de POO, eles são inicializados no começo do programa pela função run_script(), é tudo centralizado lá.
#Os personagens são salvos no arquivo de texto em forma de lista, a função run_script() pega essa lista e usa os itens pra inicializar os objetos. (dessa forma n precisa salvar o objeto, só iniciar ele sempre que rodar)

import random
import pickle
import sys
import datetime


def autoload(): #função que lê e retorna a lista de personagens do arquivo de texto
    with open ('char_doc.txt', 'rb') as fp:
        char_list = pickle.load(fp)
    return char_list


rodar = True
char_hp = 100
foe_hp = 100
att_stat = 50
char_list = autoload() #lista de personagens, ela inicia puxando do arquivo de texto por padrão
role_dict = {}
role_list = []
race_dict = {}
race_list = []


class character():
    
    def __init__(self, name, hp, att, luck, backstory, lista): #Salva os atributos como itens numa lista no arquivo txt
        self.name = name
        self.hp = hp
        self.att = att
        self.luck = luck
        self.backstory = backstory
        self.list = [self.name, self.hp, self.att, self.luck, self.backstory]
        lista.append(self.list)

    def save_char(self, lista): #Salva um personagem no arquivo de texto
        with open('char_doc.txt', 'wb') as fp:
            pickle.dump(lista, fp)
        print('Personagem salvo com sucesso!', self.name)


class char_race():
    
    def __init__(self, race_name, race_hp):
        self.hp = race_hp
        self.name = race_name
        race_dict[self.name] = self


class char_role():

    def __init__(self, role_name, role_hp_multi, role_att_multi, role_luck_multi):
        self.name = role_name
        self.hp_multi = role_hp_multi
        self.att_multi = role_att_multi
        self.luck_multi = role_luck_multi
        role_dict[self.name] = self


#class enemy():
    #pass
    #base_stats = list(0, 151)
    
    #def __init__(self, difficulty, xp_value):
        
        #random_multiplier = random.choice(base_stats)
        #if difficulty == 0:
            #self.HP = 
        #if difficulty == 1:
        
        #if difficulty == 2:
        
        #if difficulty == 3:
        
        #if difficulty == 4:
        
        #if difficulty >= 5:




def force_start():
    choice = input('Tem certeza? Seu save será PERMANENTEMENTE APAGADO (y/n) ')
    if choice.lower() == 'y':
        char_list = [str(datetime.datetime.now())]
        with open('char_doc.txt', 'wb') as fp:
            pickle.dump(char_list, fp)
        print('Save iniciado! O que foi feito não poderá ser desfeito...')
    else:
        print('. . .')


def load():
    with open ('char_doc.txt', 'rb') as fp:
        itemlist = pickle.load(fp)
        char_list = itemlist
        print(char_list[0], len(char_list) - 1, 'personagens salvos')


def save():
    with open ('char_doc.txt', 'rb') as fp:
        itemlist = pickle.load(fp)
        for i in itemlist:
            print(i)


def desenho():
    print(':-)')


def command_list(): #lista dos comandos possíveis no começo do programa
    comandos = ['dice', 'combat', 'characters', 'load']
    print('Comandos válidos:', comandos)


def create_char():
    char_att = 100
    char_luck = 100
    char_name = input('Nome do personagem: ')
    
    #SELETOR DE RAÇAS
    contador = 0
    for i in race_list:
        print(contador, ':', i)
        contador = contador + 1
    choice = int(input('Qual a raça do personagem? '))
    while choice > len(race_list):
        print('Escolha uma opção válida! ')
        choice = int(input('Qual a raça do personagem? '))
    char_hp = race_dict[race_list[choice]].hp
    
    
    #SELETOR DE CLASSES
    contador = 0
    for i in role_list:
        print(contador, ':', i)
        contador = contador + 1 
    choice = int(input('Qual a classe do seu personagem? '))
    while choice > len(role_list):
        print('Escolha uma opção válida! ')
        choice = int(input('Qual a classe do seu personagem? '))
    char_hp = role_dict[role_list[choice]].hp_multi * char_hp
    char_att = role_dict[role_list[choice]].att_multi * char_att
    char_luck = role_dict[role_list[choice]].luck_multi * char_luck
    
    backstory = input('Qual a backstory do seu personagem? ')
    
    #INICIALIZA O PERSONAGEM
    char_name = character(str(char_name), char_hp, char_att, char_luck, backstory, char_list)
    
    #SALVA A LISTA DE PERSONAGENS
    char_name.save_char(char_list)
    
    print('Personagem criado!')
    print('Nome:', char_name.name)
    print('HP:', char_name.hp)
    print('Ataque:', char_name.att)
    print('Backstory:', char_name.backstory)


def view_char():
    contador = 1
    for i in char_list[1:]:
        personagem = char_list[contador]
        print(personagem[0])
        contador = contador + 1


def view_char_stats():
    contador = 1
    for i in char_list[1:]:
        personagem = char_list[contador]
        print(contador, ':', personagem[0])
        contador = contador + 1
    char_select = input('De qual personagem? (1, 2, 3...) ')
    char_select = char_list[int(char_select)]
    print('Nome:', char_select[0])
    print('HP:', char_select[1])
    print('Ataque:', char_select[2])
    print('Backstory:', char_select[4])


def characters_menu():
    function_dict = {'create': create_char, 'view': view_char, 'stats': view_char_stats}
    function_list = []
    contador = 0
    for i in function_dict:
        function_list.append(i)
        print(contador, ':', i)
        contador = contador + 1
    choice = int(input('Selecione uma opção: '))
    if choice < len(function_list):
        function_dict[function_list[choice]]()
    else:
        characters()


def dice(): #joga os dados, mostra os resultados.
    D6 = list(range(1, 7))
    D20 = list(range(1, 21))
    D100 = list(range(1, 101))
    D4 = list(range(1, 5))
    dado_type = input('Qual dado vc quer rolar? (D4, D6, D20, D100) ')
    dado_rep = input('Quantas vezes? ')
    while dado_rep.isalpha() == True:
        print('Apenas valores numéricos!')
        dado_rep = input('Quantas vezes? ')
    dado_rep = int(dado_rep)
    while dado_rep > 0:
        if dado_type == 'd6' or dado_type == 'D6':
            dado_roll = random.choice(D6)
            print('Você rolou o número', dado_roll)
            dado_rep = dado_rep - 1
        elif dado_type == 'd20' or dado_type == 'D20':
            dado_roll = random.choice(D20)
            print('Você rolou o número', dado_roll)
            dado_rep = dado_rep - 1
        elif dado_type == 'd100' or dado_type == 'D100':
            dado_roll = random.choice(D100)
            print('Você rolou o número', dado_roll)
            dado_rep = dado_rep - 1
        elif dado_type == 'd4' or dado_type == 'D4':
            dado_roll = random.choice(D4)
            print('Você rolou o número', dado_roll)
            dado_rep = dado_rep - 1
        else:
            print('Escolha uma opção válida ou EXIT pra sair!')
            dado_rep = dado_rep - 100
            dice()
    if dado_rep <= 0:
        print('Pronto!')


def combat_dice(damage):
    D6 = list(range(1, 7))
    D20 = list(range(1, 21))
    D100 = list(range(1, 101))
    D4 = list(range(1, 5))
    dado_type = input('Qual dado vc quer rolar? (D4, D6, D20, D100) ')
    dado_rep = input('Quantas vezes? ') #define o contador (vezes que vai jogar o dado)
    while dado_rep.isalpha() == True:
        print('Apenas valores numéricos!')
        dado_rep = input('Quantas vezes? ')
    dado_rep = int(dado_rep)
    while dado_rep == 0: #loop caso o usuário escolha 0, ele precisa escolher alguem número diferente de 0
        print('Escolha quantas vezes rolar o dado! ')
        dado_rep = int(input('Quantas vezes? '))
    while dado_rep > 0: #enquanto o contador for > 0, o loop continua
        if dado_type == 'd6' or dado_type == 'D6':
            dado_roll = random.choice(D6)
            print('Você rolou o número', dado_roll)
            damage.append(dado_roll) #coloca o valor dos dados na lista 'damage'
            dado_rep = dado_rep - 1 #diminui o contador
        elif dado_type == 'd20' or dado_type == 'D20':
            dado_roll = random.choice(D20)
            print('Você rolou o número', dado_roll)
            damage.append(dado_roll)
            dado_rep = dado_rep - 1
        elif dado_type == 'd100' or dado_type == 'D100':
            dado_roll = random.choice(D100)
            print('Você rolou o número', dado_roll)
            damage.append(dado_roll)
            dado_rep = dado_rep - 1
        elif dado_type == 'd4' or dado_type == 'D4':
            dado_roll = random.choice(D4)
            print('Você rolou o número', dado_roll)
            damage.append(dado_roll)
            dado_rep = dado_rep - 1
        elif dado_type == 'exit':
            exit = 1
            while exit == 1:
                print('Saindo...')
                exit = exit + 1
                functions(input('Entre com um comando: ').lower())
        else:
            print('Escolha uma opção válida ou EXIT pra sair!')
            dado_rep = dado_rep - 100
            combat_dice(damage)
    if dado_rep <= 0: #quando o contador zera, o processo para
        print('...')


def combat(): #MODO DE COMBATE
    contador = 1
    damage = [] #INICIA A LISTA DE DANO
    foe_hp = 100
    for i in char_list[1:]:
        personagem = char_list[contador]
        print(contador, ':', personagem[0])
        contador = contador + 1
    char_select = input('Com qual personagem deseja entrar num combate?(1, 2, 3...) ')
    char_select = char_list[int(char_select)]
    while char_select[1] > 0 and foe_hp > 0:
        action = input('O que você vai fazer? (fight, run) ').lower()
        if action == 'fight':
            combat_dice(damage) #chama a função dos dados de combate
            for i in damage: #pega o resultado dos dados e passa pelo loop
                if i == damage[0]: #pro primeiro item da lista não acontece nada, pode acontecer de bugar o código com números repetidos
                    print('CALCULANDO DANO...')
                else: #pros outros itens, eles são somados ao primeiro
                    damage[0] = damage[0] + i
            att = char_select[2]/100
            real_damage = damage[0] * att
            print('O dano causado foi', real_damage) #mostra o primeiro valor
            foe_hp = foe_hp - real_damage #subtrai da vida do inimigo o dano causado
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
        if action == 'exit':
            exit = 1
            while exit == 1:
                print('Saindo...')
                exit = exit + 1
                functions(input('Entre com um comando: ').lower())
        else:
            while True:
                print('Escolha uma opção válida ou EXIT pra sair!')
                break
    if char_select[1] <= 0: #se vc morrer vc morre (ainda não tem como vc levar dano, mas vai ter)
        print('VOCÊ MORREU...') #git gud
    if foe_hp <= 0: #se o maluco morrer vc ganha
        print('VOCÊ VENCEU!!!')


def main_menu(): #literalmente o menu
    function_dict = {'force_start': force_start, 'load': load, 'save': save, 'characters': characters_menu, 'combat': combat, 'dice': dice, 'exit': main, 'secreto': desenho}
    function_list = []
    contador = 0
    for i in function_dict:
        function_list.append(i)
        print(contador, ':', i)
        contador = contador + 1
    choice = int(input('Selecione uma opção: '))
    if choice < len(function_list):
        function_dict[function_list[choice]]()
    else:
        main_menu()




def main(): #loop da UI, vc escolhe se vai continuar no loop ou terminar o programa
    while True:
        choice = input('Inserir comando? (y/n) ').lower()
        if choice == 'y':
            char_list = autoload()
            print(char_list[0], len(char_list) - 1, 'personagens salvos')
            main_menu()
        elif choice == 'n':
            print('Fim do processo')
            break
        
        else:
            print('...')
        

def run_script():
    
    #RAÇAS DO JOGO
    human = char_race('human', 100)
    elf = char_race('elf', 75)
    dwarf = char_race('dwarf', 125)
    
    #CLASSES DO JOGO
    warrior = char_role('warrior', 1.5, 1.0, 0.75) 
    mage = char_role('mage', 0.9, 1.5, 0.9)
    ranger = char_role('ranger', 0.75, 1.2, 0.85)
    
    #CRIA AS LISTAS
    for i in race_dict:
        race_list.append(i)
    
    for i in role_dict:
        role_list.append(i)
        
    #INICIALIZA OS PERSONAGENS
    with open ('char_doc.txt', 'rb') as fp:
        itemlist = pickle.load(fp)
    contador = 0
    for i in itemlist:
        if contador > 0:
            i[0] = character(i[0], i[1], i[2], i[3], i[4], autoload())
            print(i[0].name)
        contador = contador + 1
    
    
    


run_script() #INICIALIZA TODOS OS OBJETOS
main()

 