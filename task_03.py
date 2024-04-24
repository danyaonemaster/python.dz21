with open("txt4.txt", "r+") as f:
    lines = f.readlines()
    f.writelines(lines[:-1])

with open("txt5.txt", "w") as f:
    f.writelines(lines[-1])
