balance = 1000
def deposite(damount,wamount):
    global balance
    balance += damount
    balance -= wamount
    print(f"Deposited: {damount}")
    print(f"Withdrawn: {wamount}")
    print(f"New Balance: {balance}")
deposite(500, 200)

