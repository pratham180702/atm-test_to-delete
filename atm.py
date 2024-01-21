class AtmAccHolder():
    def __init__(self, name, cardNo, pin, balance):
        self.name = name
        self.cardNo = cardNo
        self.pin = pin
        self.balance = balance
    def deposit(self,deposit_amt):
        account_holder.balance += deposit_amt
        print("Balance after deposit is: ", account_holder.balance)

def deposit(account_holder, deposit_amt):
    account_holder.balance += deposit_amt
    print("Balance after deposit is: ", account_holder.balance)


def withdrawal(account_holder, withdraw_amt):
    if withdraw_amt < account_holder.balance:
        account_holder.balance -= withdraw_amt
        print("Amount to collect: ", withdraw_amt)
        print("Remaining balance is: ", account_holder.balance)
    else:
        print("Sorry, you do not have enough bank balance")


def checkbalance(account_holder):
    print("Your account's balance is: ", account_holder.balance)


# data of card holders
acc_holder_data = [
    AtmAccHolder('sakshi', "28190290188422", 3411, 5000),
    AtmAccHolder('hiya', "28190290188422", 9354, 6789),
    AtmAccHolder('pratham', "28110290198424", 6125, 2301),
    AtmAccHolder('shivali', "18190290111421", 2711, 500),
    AtmAccHolder('isha', "88192270488422", 1203, 9000),
    AtmAccHolder('keya', "98192901177222", 2121, 5353),
    AtmAccHolder('jaydeep', "58190720188429", 5901, 1000)
]

# Taking input of PIN from the user
user_pin = int(input("Please enter your 4-digit PIN correctly: "))

# Check if the entered PIN is correct
pin_correct = False
account_holder = None

for acc_holder in acc_holder_data:
    if user_pin == acc_holder.pin:
        pin_correct = True
        account_holder = acc_holder
        break

if pin_correct:
    print("PIN verified. Please enter which functionality you need ")
    print("1 for Deposit")
    print("2 for withdrawal")
    print("3 for check balance")
    user_input = int(input("Please enter which functionality you need "))

    if user_input == 1:
        deposit_amt = int(input("Enter amount you want to deposit: "))
        AtmAccHolder.deposit(account_holder, deposit_amt)
    elif user_input == 2:
        withdraw_amt = int(input("Enter amount you want to withdraw: "))
        withdrawal(account_holder, withdraw_amt)
    elif user_input == 3:
        checkbalance(account_holder)
    else:
        print("Not a valid option.")
else:
    print("Incorrect PIN. Enter a valid PIN.")
