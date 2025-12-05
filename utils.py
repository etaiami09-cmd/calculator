def string_operations():
    return dict({1:'+',2:'-',3:'*',4:'/'})
def safe_floats(number):
    if number.is_integer():
        return int(number)
    return number