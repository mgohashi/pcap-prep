

if __name__ == "__main__":
    my_str = "12345"
    print("Print the sequence: my_str = [\"12345\"] =", my_str)

    print("Print the third char. Starting with zero (0): my_str[2] =", my_str[2])

    print("Print the second char start including and ends excluding: my_str[1:2] =", my_str[1:2])

    print("Print all last 3 chars => my_str[2:] =", my_str[2:])

    print("Print the last char: my_str[-1] =", my_str[-1])

    try:
        my_str[5]
    except Exception as e:
        print("Access a non-existing char in a string ->", type(e), e)