world_old = input("Enter old world: ")
world_new = input("Enter new world: ")

with open("txt6.txt", "r") as file:
    filo = file.read().replace(world_old, world_new)

with open("txt6.txt", "w") as file:
    file.write(filo)
