f = open('hello.txt', encoding="UTF-8")

for n, line in enumerate(f, start=1):
    print(f"{n}: {line[:-1]}")

f.close()
