class Pet():
    name = 'Имя не задано'
    weight = 0.0 # kg
    voice = 'Голос не определен'
    hungry = True

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight # kg

    def feed(self):
        self.hungry = False
  
    def get_product(self):
        return 'Продукт не определен'
  
    def get_info(self):
        return f'{self.__class__.__name__} {self.name}, вес {self.weight}, накормлено {not self.hungry}, голос {self.voice}'

    def __gt__(self, other):
        return self.weight > other.weight

class Goose(Pet): # Гуси
    voice = 'Га-Га'
  
    def get_product(self):
        return 'Вы собрали гусиных яиц от гуся ' +\
               self.name
    
class Cow(Pet): # Коровы
    voice = 'Му-Му'

    def get_product(self):
        return 'Вы подоили корову ' +\
               self.name

class Sheep(Pet): # Овцы
    voice = 'Ме-Ме'

    def get_product(self):
        return 'Вы подстригли овцу ' +\
               self.name

class Сhicken(Pet): # Курицы
    voice = 'Ко-Ко'

    def get_product(self):
        return 'Вы собрали куриных яиц от курицы ' +\
               self.name

class Goat(Pet): # Козы
    voice = 'Бе-Бе'

    def get_product(self):
        return 'Вы подоили козу ' +\
               self.name

class Duck(Pet): # Утки
    voice = 'Кря-Кря'

    def get_product(self):
        return 'Вы собрали утиных яиц от утки ' +\
               self.name

pets = {
    '1': Goose('Серый', 5.5),
    '2': Goose('Белый', 5),
    '3': Cow('Манька', 250),
    '4': Sheep('Барашек', 40),
    '5': Sheep('Кудрявый', 45),
    '6': Сhicken('Ко-ко', 2.0),
    '7': Сhicken('Кукареку', 2.5),
    '8': Goat('Рога', 25),
    '9': Goat('Копытка', 20),
    '10': Duck('Кряква', 4)
    }

commands = {
    'f': 'feed - кормить',
    'g': 'get - получать продукты',
    'v': 'voice - слушать голоса животных',
    'i': 'info - получить полную инофрмацию о животном',
    'c': 'calculate weight - посчитать общий вес всех животных',
    'h': 'heaviest - узнать самое тяжелое животное на ферме',
    'q': 'quit - покинуть ферму',
    }

def get_heaviest():
    heaviest_pet = Pet('', 0.0)
  
    for key in pets:
        if pets[key] > heaviest_pet:
            heaviest_pet = pets[key]
  
    return heaviest_pet

def get_total_weight():
    total_weight = 0
    for key in pets:
        total_weight += pets[key].weight
    return total_weight

def print_pets():
    for key in pets:
        print(f'  {key}: {pets[key].__class__.__name__} {pets[key].name}')

def print_commands():
    for key in commands:
        print(f'  {key}: {commands[key]}')

def main():
    print('Что будем делать на ферме?')
    print_commands()
    while True:
        command = input('\nВыберете действие (\"r\" повторно вывести список действий): ').strip()
        
        if command == 'f':
            print('Кого будем кормить?')
            print_pets()
            pet_key = input().strip()
            if pet_key not in pets.keys():
                print('\nНомер животного введен неправильно. Начните заново')
                continue
            pets[pet_key].feed()
            if not pets[pet_key].hungry:
                print(f'  {pets[pet_key].__class__.__name__} {pets[pet_key].name} накормлено')

        elif command == 'g':
            
            print('От кого будем получать продукты?')
            print_pets()
            pet_key = input().strip()
            if pet_key not in pets.keys():
                print('\nНомер животного введен неправильно. Начните заново')
                continue
            print(pets[pet_key].get_product())

        elif command == 'v':
            print('Кого будем слушать?')
            print_pets()
            pet_key = input().strip()
    
            if pet_key not in pets.keys():
                print('\nНомер животного введен неправильно. Начните заново')
                continue
            print(pets[pet_key].voice)

        elif command == 'i':
            print('О ком нужна информация?')
            print_pets()
            pet_key = input().strip()
            if pet_key not in pets.keys():
                print('\nНомер животного введен неправильно. Начните заново')
                continue
            print(pets[pet_key].get_info())

        elif command == 'c':
        
            print(f'Общий вес животных {get_total_weight()} кг')
    
        elif command == 'h':
    
            heaviest = get_heaviest()
            print(f'Самое тяжелое животное - {heaviest.__class__.__name__} {heaviest.name}, вес {heaviest.weight} кг')
    
        elif command == 'r':
            print('Что будем делать на ферме?')
            print_commands()
            continue
        elif command == 'q':
            break
        else:
            print('\nВведена неизвестная команда. Повторите выбор действия или введите \"r\" для повторного вывода списка действий')
  
main()