from typing import List
from random import randrange
from math import atan2


def counterclockwise_sort(n: int) -> List[int]:
    # Генерируем точки
    points = [(randrange(-100, 100), randrange(-100, 100)) for i in range(n)]
    first_square, second_square, third_square, fouth_square = [], [], [], []
    sorted_counterclockwise = []

    # Раскидываем точки по четвертям
    for point in points:
        if point[0] > 0 and point[1] > 0:
            first_square.append(point)
        elif point[0] <= 0 and point[1] >= 0:
            second_square.append(point)
        elif point[0] <= 0 and point[1] <= 0:
            third_square.append(point)
        else:
            fouth_square.append(point)

    # Находим первую точку. с которой будет обход против часовой стрелке
    first_square.sort(key=lambda i: i[0])
    sorted_counterclockwise.append(first_square[0])
    first_square = first_square[1:]
    # Сортируем точки в четвертях против часовой стрелке
    first_square.sort(key=lambda i: atan2(i[1], i[0]))
    second_square.sort(key=lambda i: atan2(i[1], i[0]))
    third_square.sort(key=lambda i: atan2(i[1], i[0]))
    fouth_square.sort(key=lambda i: atan2(i[1], i[0]))

    sorted_counterclockwise += second_square + third_square + \
        fouth_square + first_square
    return sorted_counterclockwise


def calculate_distances(list_points: List[int]) -> str:
    # Находим расстояние от центра координат (0, 0) до каждой точки
    distances = \
        [(point[0] ** 2 + point[1] ** 2) ** 0.5 for point in list_points]

    output = [round(min(distances), 2),
              round(max(distances), 2),
              round(sum(distances)/len(distances), 2)]
    return f'Мин.: {output[0]} \nМакс.: {output[1]}\nСреднее: {output[2]}'

if __name__ == '__main__':
    print('Введите количество точек:')
    n = int(input())
    counterclockwise_points = counterclockwise_sort(n)
    print(calculate_distances(counterclockwise_points))
