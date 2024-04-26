world = input("Enter the world: ")

with open("txt8.txt", "r") as file:
    file = file.read().split()

print(len([i for i in file if i == world]))
