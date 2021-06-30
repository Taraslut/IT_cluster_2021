from deco import deco


def catch(foo, values={}):
    def inner(*args, **kwargs):
        if args not in values:
            values[args] = foo(*args)
        return values[args]
    return inner

# @deco
@catch
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


if __name__ == "__main__":
    print(fib(800))
    # print(fib(10))
