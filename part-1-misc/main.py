from datetime import date
import math
import random

if __name__ == "__main__":
    print("## Basic types")

    my_str = "12345"

    print("Test data: my_str = [\"12345\"] =", my_str)

    print("Print the third char. Starting with zero (0): my_str[2] =", my_str[2])

    print("Print the second char start including and ends excluding: my_str[1:2] =", my_str[1:2])

    print("Print all last 3 chars => my_str[2:] =", my_str[2:])

    print("Print the last char: my_str[-1] =", my_str[-1])

    a_num = -10.1
    b_num = 20.5
    c_str = '10'
    d_str = '10'
    e_num = 4
    f_num = 2

    print("## Basic Operations")
    print("Test data: a_num, b_num, c_str, d_str, e_num, f_num =",
          [a_num, b_num, c_str, d_str, e_num, f_num])

    print("e_num // f_num:", e_num // f_num)
    print("e_num ** f_num:", e_num ** f_num)

    print()
    print("## Sum nums and str")
    print("Test data [a_num, b_num, c_str, d_str] =", 
          [a_num, b_num, c_str, d_str])

    print("Print the sum of a_num and b_num =", a_num + b_num)
    
    try:
        print(c_str + a_num)
    except TypeError as e:
        print("TypeError sum c_str and a_num =", e)

    try:
        print(a_num + c_str)
    except TypeError as e:
        print("TypeError sum a_num and c_str =", e)

    print("Print the sum of c_str and d_str =", c_str + d_str)

    print()
    print("## Math module")

    print("Print the fabs of the sum of a_num and b_num =", 
          math.fabs(a_num + b_num))
    
    print("Print the floor of the a_num =", math.floor(a_num))

    print("Print the ceil of the b_num =", math.ceil(b_num))
    
    print()
    print("## Random module")

    print("Print the basic random [0 - 1] =", random.random())

    print("Print a random in a range [1 - <11] =", random.randrange(1, 11))

    print("Print a random in a range with step =", random.randrange(1, 6, 2))

    my_list = [1,2,3,4,5,6,7,8]
    print("Test data my_list =", my_list)

    random.shuffle(my_list)
    print("Print shuffle of a my_list =", my_list)

    sample = random.sample(my_list, 3)
    print("Print a sample list of 3 elements =", sample)

    my_fruits = ["apple", "orange", "grape", "banana"]
    print("Print my_fruits =", my_fruits)
    print("Print the choice for my_fruits =", random.choice(my_fruits))

    my_seed = 232
    print("Print my_seed =", my_seed)
    random.seed(my_seed)
    print("Print a reproducible random =", random.random())

    print()
    print("## Lists")
    my_list = [1, 2, 3, 4, 5, 6, 7]
    print("Test data my_list =", my_list)
    print("Print last element my_list[-1] =", my_list[-1])
    try:
        print(my_list[-8])
    except Exception as e:
        print("Print first element my_list[-8] =", type(e), e)
    print("[x * \"a\" for x in my_list] =", [x * "a" for x in my_list])

    print()
    print("## Tuples")
    my_tuple = (100, "apple", 40.5, date(2023, 10, 1))
    print("Test data my_tuple =", my_tuple)

    print("Print first element my_tuple[0] =", my_tuple[0])
    print("Print last element my_tuple[-1] =", my_tuple[-1])
    print("Gen new tuple from my_tuble[0::2] =", my_tuple[0::2])