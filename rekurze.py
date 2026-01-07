from turtle import *

def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)

def find_min(list):
    first_half = list[:len(list)//2]
    second_half = list[len(list)//2:]

    if len(list) == 1:
        return list[0]
    return min(find_min(first_half), find_min(second_half))

def fractal_tree(lenght):
    if lenght < 1:
        return
    forward(lenght)
    left(45)
    fractal_tree(lenght/4)
    right(90)
    fractal_tree(lenght/4)
    left(45)
    backward(lenght)

fractal_tree(200)
#mesmerising_list = [1, 2, 3, 0.05, -1, 4, 0.5]
#print(find_min(mesmerising_list))