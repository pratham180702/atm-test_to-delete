class AtmAccHolder:
    def __init__(self, name, cardNo, pin, balance):
        self.name = name
        self.cardNo = cardNo
        self.pin = pin
        self.balance = balance

    def deposit(self, deposit_amt):
        self.balance += deposit_amt
        print("OPERATION SUCCESSFUL!")
        print("Balance after deposit is: ", self.balance)

    def checkbalance(self):
        print("Current balance is: ", self.balance)

    def withdraw(self, withdraw_amt):
        self.balance -= withdraw_amt
        print("OPERATION SUCCESSFUL!")
        print("Balance after withdrawal is: ", self.balance)


def initialize_account_data():
    return [
        AtmAccHolder('sakshi', "28190290188422", 3411, 5000),
        AtmAccHolder('hiya', "28190290188422", 9354, 6789),
        AtmAccHolder('pratham', "28110290198424", 6125, 2301),
        AtmAccHolder('shivali', "18190290111421", 2711, 500),
        AtmAccHolder('isha', "88192270488422", 1203, 9000),
        AtmAccHolder('keya', "98192901177222", 2121, 5353),
        AtmAccHolder('jaydeep', "58190720188429", 5901, 1000)
    ]


# Load data from the file at the start of the program
acc_holder_data = []
try:
    with open('account_data.txt', 'r') as file:
        for line in file:
            name, cardNo, pin, balance = line.strip().split(',')
            acc_holder_data.append(AtmAccHolder(name, cardNo, int(pin), int(balance)))
except FileNotFoundError:
    # Handle the case where the file doesn't exist (first run of the program)
    acc_holder_data = initialize_account_data()

user_pin = int(input("Please enter your 4-digit PIN correctly: "))

pin_correct = False

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
    print("4 to exit")
    user_input = int(input("Please enter which functionality you need "))

    while user_input != 4:
        if user_input == 1:
            deposit_amt = int(input("Enter amount you want to deposit: "))
            account_holder.deposit(deposit_amt)
        elif user_input == 2:
            withdraw_amt = int(input("Enter amount you want to withdraw: "))
            account_holder.withdraw(withdraw_amt)
        elif user_input == 3:
            account_holder.checkbalance()
        else:
            print("Not a valid option.")

        # Save the updated data to the file
        with open('account_data.txt', 'w') as file:
            for acc_holder in acc_holder_data:
                file.write(f"{acc_holder.name},{acc_holder.cardNo},{acc_holder.pin},{acc_holder.balance}\n")

        print("1 for Deposit")
        print("2 for withdrawal")
        print("3 for check balance")
        print("4 to exit")
        user_input = int(input("Please enter which functionality you need "))

    print("THANK YOU FOR USING 's ATM")

else:
    print("Incorrect PIN. Enter a valid PIN.")
