with open("txt1.txt", "r") as f_1:
    f_1 = f_1.readlines()
with open("txt2.txt", "r") as f_2:
    f_2 = f_2.readlines()

different_lines_file1 = [line for line in f_1 if line not in f_2]
different_lines_file2 = [line for line in f_2 if line not in f_1]

if different_lines_file1 == different_lines_file2:
    print("both files are the same")
else:
    print(f"files1 are different: {" ".join(different_lines_file1)}\n"
          f"files2 are different: {" ".join(different_lines_file2)}")