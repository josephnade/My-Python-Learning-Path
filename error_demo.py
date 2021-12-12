list = ["1", "2", "5a", "10b", "abc"]
list2 = []
# Find numeric data in list
for i in list:
    try:
        result = int(i)
    except Exception:
        continue
    else:
        list2.append(result)
print(list2)
# Check user enter numeric numbers all the time except enter 'q' unless throw exception
while True:
    result = input("Please enter a number. If you want to exit please press 'q' = ")
    try:
        int(result)
        print("It is a number")
    except ValueError as e:
        if result == 'q':
            print("Have a good day!")
            break
        else:
            print("Please enter a number")


# Check the password is not include Turkish letter.
def check_password(psw):
    import re
    if re.search("[ı,İ,ğ,Ğ,ü,Ü,ş,Ş,ö,Ö,ç,Ç]", psw):
        raise Exception("Password can not include Turkish case!")


while True:
    password = input("Please enter a password: ")
    try:
        check_password(password)
    except Exception as e:
        print(e)
    else:
        print("Password is valid.")
        break


# Create factorial function and throw error message for incoming value from function.
def fac(x):
    if x == 1:
        return x
    elif x < 0:
        raise Exception("You can not enter negative number.")
    else:
        return x * fac(x - 1)


while True:
    try:
        result = int(input("Enter a number ="))
        print(fac(result))
    except ValueError as a:
        print("You can not enter letter.")
    except Exception as a:
        print(a)
    else:
        break
