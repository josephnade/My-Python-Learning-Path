def withdraw(account, amount):
    print(f"Hello {account['name']}")
    if amount > account['balance']:
        while True:
            answer = input("Your balance can not afford it. Do you want to use extra balance.(y = yes) (n = no):")
            if answer == "y":
                if amount > account['balance'] + account['extraBalance']:
                    print("You can not withdraw this amount because your balance and extra balance can not afford.")
                    break
                else:
                    account['extraBalance'] -= (amount - account['balance'])
                    account['balance'] = 0
                    print(f"You withdrawed {amount} money. New extra balance is: {account['extraBalance']} ")
                    break
            elif answer == "n":
                print("Have a good day!")
                break
            else:
                print("You entered wrong input. Please enter correct letter!")
    else:
        account['balance'] -= amount
        print(f"You withdrawed {amount} money. New balance is: {account['balance']}")


def deposit(account, amount):
    print(f"Hello {account['name']}.")
    while True:
        answer = input("[1]Balance\n[2]Extra Balance\nWhich balance do you want to deposit ->")
        if answer == '1':
            account['balance'] += amount
            print(f"You deposited {amount} money. New balance is {account['balance']}")
            break
        elif answer == '2':
            account['extraBalance'] += amount
            print(f"You deposit {amount} money. New Extra balance is {account['extraBalance']}")
            break
        else:
            print("You entered wrong number. Please try again!")


def show_balance(account):
    return account['balance']

yusufAccount = {"name": "Yusuf", "accountNo": "223142323", "balance": 50000, "extraBalance": 30000}
while True:
    answer = input("[1]Withdraw\n[2]Deposit\n[3]Show Balance\nSelect option do you want:")
    if answer == '1':
        amount = int(input("How much money dou you want to withdraw: "))
        withdraw(yusufAccount, amount)
        break
    elif answer == '2':
        amount = int(input("How much money dou you want to deposit: "))
        deposit(yusufAccount, amount)
        break
    elif answer == '3':
        show_balance(yusufAccount)
        break
    else:
        print("You entered wrong number. Please try again!")
