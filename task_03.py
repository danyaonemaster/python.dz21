with open("txt5.txt", "r") as f:
    lines = f.readlines()

with open("txt5.txt", "w") as f:
    f.writelines(lines[:-1])

with open("txt6.txt", "w") as f:
    f.writelines(lines[-1])
