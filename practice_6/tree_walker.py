from os.path import isfile, isdir, getctime, getmtime, getsize
from pathlib import Path
from os import listdir

import time

# Todo
# Спілкування з користувачем
# організувати у вигляді наступного меню:
#
# 1. Вивести вміст каталога
# 2. Змінити робочий каталог (".." - перейти в батьківський елемент)
# 3. Видрукувати файл на екран
# 4. Вийти


print(__file__)
base_file = Path(__file__).resolve()

print(base_file)

base_dir = base_file.parent.parent

print(base_dir)

# new_path = base_parent / "hello" / "world.txt"
# print(new_path)
dir_content = listdir(base_dir)

print("=" * 10, base_dir, "=" * 10)

ansestor = ''
for item in dir_content:
    creat_time = time.ctime(getctime(base_dir / item))

    if isfile(base_dir / item):
        print(item.lower(), getsize(base_dir / item), "b", creat_time)
    else:
        ansestor = item
        print(item.upper(), "== DIR ==", creat_time)

# # change dir
# ansestor_dir = base_parent / ansestor
# print("\t", "="*10, ansestor_dir, "="*10)
# for item in listdir(ansestor_dir):
#     print("\t\t", end="")
#     creat_time = time.ctime(getctime(ansestor_dir / item))
#
#     if isfile(ansestor_dir / item):
#         print(item.lower(), getsize(ansestor_dir / item), "b", creat_time )
#     else:
#         print(item.upper(), "== DIR ==", creat_time)


# file type to screen
while True:
    file_to_read = input("Which file you want ot print?")
    try:
        f = open(base_dir / file_to_read, 'r')
        for i in f:
            print(i, end="")
        break
    except FileNotFoundError:
        print("!!!! Such file do not exist")
        print("Try again")

    except PermissionError:
        print("You are going to read folder. It's impossible")
        print("Try again")

    except Exception:
        print("Something wrong!")
        print("Try again")

    time.sleep(30)
