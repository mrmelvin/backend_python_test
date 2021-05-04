## Задание 1

Используемые модули: matplotlib  
Описание установки: https://matplotlib.org/stable/users/installing.html  
Решение первого задания отображено в файле **first_task.py**  
Файл **vizualization_first_task.py** служит для своеобразной проверки выполнения **first_task.py**, помогая визуализировать вывод программы.


## Задание 2

Проверка автомобильных номеров Типа 1А.  
Данные номера имеют формат вида:  
**С227НА69**  
ГОСТом для использования на знаках разрешены 12 букв кириллицы, имеющие графические аналоги в латинском алфавите — А, В, Е, К, М, Н, О, Р, С, Т, У и Х
Коды субъектов РФ взяты отсюда:
https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%B4%D1%8B_%D1%81%D1%83%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B9_%D0%A4%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8

Для проверки созданые три функции:
+ generate_auto_number (генерируем формат типа 1А)
+ generate_incorrect_auto_number (генерируем номер похожий, но не верный по формату, используя весь русский алфавит и не отслеживая коды регионов РФ)
+ generate_random_strings (генерация строк из случайного набора символов)
