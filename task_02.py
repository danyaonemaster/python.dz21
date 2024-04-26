vowels = 'aeiouAEIOU'
consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
digits = '0123456789'

with open("txt3.txt", 'r') as f:
    file = f.read()

with open("txt4.txt", 'w') as f:
    f.write(f"file len: {len(file)}\n")
    f.write(f"Number of rows: {file.count('\n')+1}\n")
    f.write(f"Number of vowels: {sum(1 for char in file if char in vowels)}\n")
    f.write(f"Number of consonant letters: {sum(1 for char in file if char in consonants)}\n")
    f.write(f"Number of digits: {sum(1 for char in file if char in digits)}\n")
