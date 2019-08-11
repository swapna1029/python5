num= input("Type in: ")
odd = [i for i in num.split(',') if (int(i) % 2 != 0)]
print((" ").join(odd))
