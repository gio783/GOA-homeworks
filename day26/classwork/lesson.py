def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return"odd"
    

def number_to_string(num):
    return str (num)

def make_negative( number ):
    if number <= 0:
        return number
    else:
        return number * (-1)
#---------------------------------

def positive_sum(arr):
    return sum(num for num in arr if num>0)

def repeat_str(repeat, string):
    return string * repeat

def string_to_number(s):
    return int(s)