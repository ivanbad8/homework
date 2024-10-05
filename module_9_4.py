# Lambda-функция:
import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

my_func = lambda x, y: x == y

result = list(map(my_func, first, second))
print(result)


# Замыкание:

def get_advanced_writer(file_name):
    file = open(file_name, 'a+')
    file.close()

    def write_everything(*data_set):
        for sting in data_set:
            file = open(file_name, 'a', encoding='utf-8')
            file.write(str(sting) + '\n')
            file.close()

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__:

from random import choice
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
