
ll = ['animals', 'fruits', 'vegetables']

with open('www.txt', encoding="UTF-8", mode='r') as f:
    text = f.read()
    for line in text.split("\n"):
        print(line)

