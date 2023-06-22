
def try_me(my_func):
    try:
        print("Execute code", my_func)
        my_func()
    except Exception as e:
        print("Exception was raised", e)
    else:
        print("Nothing went wrong")
    finally:
        print("Finalize")

if __name__ == "__main__":
    def module_error():
        math.ceil(1.1)

    try_me(module_error)

    def divide_by_zero():
        1 / 0

    try_me(divide_by_zero)

    def success_exec():
        print("Executed successfully")

    try_me(success_exec)