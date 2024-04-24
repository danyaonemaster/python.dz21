with open("txt6.txt", "r") as file:
    file = file.read().split()

print(max([len(i) for i in file]))
