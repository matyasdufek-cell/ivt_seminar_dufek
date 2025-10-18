def is_prime(number):
    if number > 1:
        divider = 2
        while divider < number:
            if number % divider == 0:
                return False
            else:
                divider += 1
        return True
    else:
        return False

def closest_prime(number):
    if number > 1:
        while is_prime(number) == False:
            number -= 1
        return number
    else:
        return

users_number = int(input("Type in any number: "))
if closest_prime(users_number) is None:
    print("There is no prime number of lower or same value.")
else:
    print(f"Closest prime number of lower or same value is {closest_prime(users_number)}.")

    

def draw_chessboard(side_size, pattern_size):
    for i in range(side_size):
        for _ in range(pattern_size):
            for j in range(side_size):
                if ((i % 2 == 0) and (j % 2 == 0)) or ((i % 2 == 1) and (j % 2 == 1)):
                    symbol = "#"
                else: 
                    symbol = "@"
                print(pattern_size * symbol, end="")
            print()

draw_chessboard(5, 1)
draw_chessboard(3, 4)



def get_total_distance(list1, list2):
    list1.sort()
    list2.sort()
    if len(list1) == len(list2):
        total_distance = 0
        for i in range(len(list1)):
            total_distance += abs(list1[i] - list2[i])
        return total_distance
    else:
        return None

print(get_total_distance([3,5,2,1],[4,3,4,3]))