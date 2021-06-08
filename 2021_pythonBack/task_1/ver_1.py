from random import randint
import numpy as np


def generate_random_array(num_point=10):
    random_list = []
    if num_point == 0 or type(num_point) == float or num_point <= 0:
        print("Количество точек не может быть равно нулю, быть отрицательным или нецелочисленным")
    else:
        for i in range (num_point):
            random_point = [randint(-100, 100), randint(-100, 100)]
            random_list.append(random_point)
        random_array = np.array(random_list)
    #print(random_array)
    #print(random_array.shape)
    return random_array

def locate_points(random_array):
    first_quarter = []
    second_quarter = []
    third_quarter = []
    fourth_quarter = []
    for num in num_point:
        for point in random_array[n]:
            if point[0] > 0 and point[1] > 0:
                first_quarter.append(point)
            elif point[0] < 0 and point[1] > 0:
                second_quarter.append(point)
            elif point[0] < 0 and point[1] < 0:
                third_quarter.append(point)
            else:
                fourth_quarter.append(point)
    return first_quarter, second_quarter, third_quarter, fourth_quarter

num_point = int(input("Задайте количество чисел в списке: "))
generate_random_array(num_point=num_point)
