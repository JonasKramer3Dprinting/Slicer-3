def f2(d):
    return 2**d

def f3(d):
    return 3**d

def f5(d):
    return 5**d

def f7(d):
    return 7**d

def add_function(f,g):
    return f(2) + g(2)

print(add_function(lambda x: 2 ** x, lambda x: 3 ** x))
print(add_function(lambda x: 5 ** x, lambda x: 7 ** x))