from typing import List
import re
from random import choice, randint, sample, shuffle


'''
Принцип работы check_auto_numbers:
Приходящий автомобильный номер разделяется на две части:
часть самого номера, формат А123АА,
и код региона.
Делаем это чтобы немного разгрузить код и сделать более читаемым
Допустимые буквы в номере: [А, В, Е, К, М, Н, О, Р, С, Т, У, Х]
С кодом региона посложнее, допустим диапазон от 01 до 99 включительно,
также следующий список:
[102, 113, 116, 121, 122, 123, 124, 125, 126, 134, 136, 138, 142, 147, 150,
 152, 154, 156, 159, 161, 163, 164, 173, 174, 177, 178, 186, 190, 193, 197,
 198, 199, 702, 716, 750, 761, 763, 774, 777, 790, 797, 799]
'''


def check_auto_numbers(list_numbers: List[str]) -> List[str]:
    correct_number = []
    for number in list_numbers:
        check_main_number = \
            re.compile('^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}')
        check_region_code = \
            re.compile('^1(?:02|13|16|21|22|23|24|25|26|34|36|38|42|47|50|52|54|56|59|61|63|64|73|74|77|78|86|90|93|97|98|99)$|^7(?:02|16|50|61|63|74|77|90|97|99)$|^\d{2}$')
        main_number, region_code = number[:6], number[6:]
        if re.search(check_main_number, main_number) and \
                re.search(check_region_code, region_code):
            correct_number.append(number)
    return correct_number


if __name__ == '__main__':
    # Для проверки напишем две функции:
    # первая будет генерировать номера, соответствующие формату
    # вторая будет генерировать будет генерировать несколько похожие данные,
    # но при этом использовать весь русский алфавит
    # и выхоить за допустимый диапазон кода региона
    def generate_auto_number() -> str:
        available_alphabet = \
            ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']
        available_region_code = \
            ['0' + str(i) if i < 10 else str(i) for i in range(100)] + \
            [102, 113, 116, 121, 122, 123, 124, 125, 126, 134, 136, 138,
             142, 147, 150, 152, 154, 156, 159, 161, 163, 164, 173, 174,
             177, 178, 186, 190, 193, 197, 198, 199, 702, 716, 750, 761,
             763, 774, 777, 790, 797, 799]
        return '{0}{1}{2}{3}'.format(choice(available_alphabet),
                                     randint(100, 1000),
                                     ''.join(sample(available_alphabet, 2)),
                                     choice(available_region_code))

    def generate_incorrect_auto_number() -> str:
        russian_uppercase = [chr(randint(1040, 1071)) for i in range(30)]
        return '{0}{1}{2}{3}'.format(choice(russian_uppercase),
                                     randint(100, 1000),
                                     ''.join(sample(russian_uppercase, 2)),
                                     randint(0, 1000))

    # Генерируем строку из случайного набора букв, чисел и символов
    def generate_random_strings(min_word_len=8,
                                max_word_len=10,
                                words_count=15) -> List[str]:
        words = []
        for word in range(words_count):
            word = ''
            for i in range(randint(min_word_len, max_word_len)):
                word += chr(randint(33, 122))
            words.append(word)
        return words

    samples_auto_numbers = \
        [generate_auto_number() for i in range(20)] + \
        [generate_incorrect_auto_number() for i in range(20)] + \
        generate_random_strings(max_word_len=16, words_count=100)
    shuffle(samples_auto_numbers)
    print(check_auto_numbers(samples_auto_numbers))
