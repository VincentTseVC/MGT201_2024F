age = input("Enter your age: ")
while not age.isdigit() or int(age) < 1:
    print('Invalid age, TMD 你在幹什麼??? 年齡只能是數字啊!!! 而且要大於0啊')
    age = input("Enter your age (Again): ")

age = int(age)

age += 1
print("Next year, you will be " + str(age) + " years old")