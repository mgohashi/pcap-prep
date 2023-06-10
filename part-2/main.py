from MyModule.helper import find_vowels, remove_vowels


if __name__ == "__main__":
    my_str = "my target is the certification"
    print("my_str: ", my_str)

    print("remove_vowels:", remove_vowels(my_str))

    print("find_vowels:", find_vowels(my_str))