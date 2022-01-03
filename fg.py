def f(x):
    result = 2 * x + 7
    return result


def g(x):
    result = x**2
    return result


def ff(x):
    print(x + 15)
    

def gg(x):
    return x + 15    

x = 2
y = ff(x)
z = gg(x)

print(f(x) + g(x) + f(g(x)) + g(f(x)))
print(y)
print(z)