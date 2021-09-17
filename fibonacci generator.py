import collections.abc
#my fibonacci function using yield
def fibgen() -> collections.abc.Iterable:
    a = 0
    b = 1
    counter = 0
    yield a
    yield b
    while a<1000:
        yield a+b
        if counter == 0:
            a+=b
            counter = 1
        elif counter == 1:
            b+=a
            counter = 0

for fib_number in fibgen():
    print(fib_number)

#fibonacci list comprehension
series = []
series.append(0)
series.append(1)
[series.append(series[k-1] + series[k-2]) for k in range(2,10)]
print(series)

#I need to see more list comprehension to understand the variety of ways it can be used.


