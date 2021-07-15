import datetime


def function_time(function):
    # Данная "обёртка" принимает любые аргументы
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        function(*args, **kwargs)
        print(datetime.datetime.now()-start_time)

    return wrapper


@function_time
def nums_to_squares(n):
    y = []
    x = {i: i ** i for i in range(n)}
    z = {i: i ** i for i in range(n+1)}
    t = {i: i ** i for i in range(n+2)}
    y.append(x)
    y.append(z)
    y.append(t)

    return y


print(nums_to_squares(12))
