from random import randint

CHARACTER_CLASSES = {

    'warrior': {
        'attack': (5, (3, 5)),
        'defence': (10, (5, 10)),
        'special': ('Выносливость', 80 + 25),
        'description': 'Воитель — дерзкий воин ближнего боя. Сильный, выносливый и отважный.',
        'sub_description': 'ты Воитель — отличный боец ближнего боя.'
    },

    'mage': {
        'attack': (5, (5, 10)),
        'defence': (10, (-2, 2)),
        'special': ('Атака', 5 + 40),
        'description': 'Маг — находчивый воин дальнего боя. Обладает высоким интеллектом.',
        'sub_description': 'ты Маг — превосходный укротитель стихий.'
    },

    'healer': {
        'attack': (5, (-3, -1)),
        'defence': (10, (2, 5)),
        'special': ('Защита', 10 + 30),
        'description': 'Лекарь — могущественный заклинатель. Черпает силы из природы, веры и духов.',
        'sub_description': 'ты Лекарь — чародей, способный исцелять раны.'
    }
}

def attack(char_name, char_class):
    base_damage, damage_range = CHARACTER_CLASSES[char_class]['attack']
    return f"{char_name} нанёс урон противнику равный {base_damage + randint(*damage_range)}"
    
def defence(char_name, char_class):
    base_defence, defence_range = CHARACTER_CLASSES[char_class]['defence']
    return f"{char_name} применяет защиту равную {base_defence + randint(*defence_range)}"
    
def special(char_name, char_class):
    special_name, special_range = CHARACTER_CLASSES[char_class]['special']
    return f"{char_name} применил специальное умение {special_name} с силой {special_range}"

def start_training(char_name, char_class):

    commands = {
        'attack': attack,
        'defence': defence,
        'special': special
    }

    print(f"{char_name}, {CHARACTER_CLASSES[char_class]['sub_description']}")

    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, defence — чтобы блокировать атаку противника или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')

    cmd = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd in commands:
            print(commands[cmd](char_name, char_class))
        elif cmd != 'skip':
            print('Неизвестная команда. Попробуйте снова.')
    return 'Тренировка окончена.'

def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        flag = True
        while flag:
            char_class = input('Введи название персонажа, за которого хочешь играть: Воитель — warrior, Маг — mage, Лекарь — healer: ')
            if char_class in CHARACTER_CLASSES:
                print(CHARACTER_CLASSES[char_class]['description'])
                flag = False
            else:
                print('Такого класса не существует. Попробуйте ещё раз.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, чтобы выбрать другого персонажа ').lower()
    return char_class

def name_checker(char_name: str) -> str:
    if char_name == "" or char_name == " ":
        return "Игрок"
    
    return char_name.replace(" ", "").capitalize()

def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = name_checker(input('...назови себя: '))
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))
    
main()
