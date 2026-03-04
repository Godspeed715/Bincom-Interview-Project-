with open("./name.txt") as file:
    data = file.readline().strip().split(" ")

for name in data:
    print(name)