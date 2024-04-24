with open("txt4.txt", "r") as f_1:
    f_1 = f_1.readlines()

f_1.pop()

with open("txt5.txt", "w") as f_2:
    f_2 = f_2.writelines(f_1)