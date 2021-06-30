def deco(foo):
    def inner(*args, **kwargs):
        print(f"Call {foo.__name__} with Params args={args}, kwargs={kwargs}")
        rez = foo(*args)
        # print(f'{foo.__name__} return {rez}')
        return rez
    return inner


def info(foo):
    def inner(*args, **kwargs):
        print("In the info")
        rezz = foo(*args)
        print("In the info after call.")
        return rezz
    return inner


@info
@deco
def say_hello(name):
    return f'Hello {name}!!!! \nNice to see you {name}.'


if __name__ == "__main__":
    print(say_hello("Taras"))

import functools
