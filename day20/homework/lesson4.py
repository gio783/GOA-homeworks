mixed_list = [123, "hello", 45.6, True, "python", [1,2,3], "world"]

def new_func(mixed_list):
    for item in mixed_list:
        if isinstance(item, str):
            print(item.upper()[-3:])

