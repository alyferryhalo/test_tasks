# генерация списка координат: версия 0.0

from random import randint

def main():
    n = int(input("Задайте количество чисел в списке: "))
    random_list = []
    if n == 0 or type(n) == float or n <= 0:
        print("Количество точек не может быть равно нулю, быть отрицательным или нецелочисленным")
    else:
        for i in range (n):
            random_point = [randint(-100, 100), randint(-100, 100)]
            random_list.append(random_point)
        print(random_list)

if __name__ == "__main__":
    main()
