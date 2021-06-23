import sys


def my_print(list_obj):
    ss = ""
    for i in list_obj:
        ss += i + "\n"
        print(i)
    return ss


def summa(a, b):
    return a + b

print("2"*100)
print(__name__)

if __name__ == "__main__":
    print("3"*100)
    var = sys.path

    print(var)

    print(sys.path)

    name = 'c:\\name'
    print(name)

    assert summa(2, 4) == 6
    assert my_print(['one', 'second']) == "one\nsecond\n"
