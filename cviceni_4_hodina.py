list_of_numbers = [1, 2, 3, 4]

def soucet(seznam):
    sum = 0
    for number in seznam:
        sum += number
    return sum

def nejvyssi(seznam):
    highest_number = seznam[0]
    for number in seznam:
        if number > highest_number:
            highest_number = number
    return highest_number

def vyskytuje_se (seznam, hodnota):
    if hodnota in seznam:
        return True

print(soucet(list_of_numbers))
print(nejvyssi(list_of_numbers))
print(vyskytuje_se(list_of_numbers, 1))
print(vyskytuje_se(list_of_numbers, 0))