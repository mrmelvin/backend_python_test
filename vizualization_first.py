from first_task import counterclockwise_sort, calculate_distances
import matplotlib.pyplot as plt


if __name__ == '__main__':
    n = int(input())
    counterclockwise_points = counterclockwise_sort(n)
    print(calculate_distances(counterclockwise_points))
    
    # Строим обход точек против часовой стрелке
    x = [i[0] for i in counterclockwise_points]
    y = [i[1] for i in counterclockwise_points]
    plt.xlabel("x") 
    plt.ylabel("y") 
    plt.grid()   
    plt.plot(x, y)
    for point_x, point_y in counterclockwise_points:
        plt.text(point_x, point_y, f'({point_x},{point_y})')   
    plt.show()