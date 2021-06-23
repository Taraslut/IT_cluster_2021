from random import randint

random_number = randint(1, 50)
count = 10

print(random_number)
while count:
    number = int(input(">>"))
    if number > random_number:
        print("my number is less")
        count -= 1
    elif number < random_number:
        print("my number is bigger")
        count -= 1
    elif number == random_number:
        count = 0

print("end")
