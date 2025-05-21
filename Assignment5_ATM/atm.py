class ATM:
    def __init__(self):
        self.balance = 5000
        self.pin = 1234
        self.is_authenticated = False

    def check_pin(self, input_pin):
        
            if input_pin == self.pin:
                self.is_authenticated = True
                print(" PIN verified successfully.")
            else:
                print(" Invalid PIN. Please try again.")
                main()


    def check_balance(self):
        if self.is_authenticated:
            print(f" Your current balance is: {self.balance} rupees")
        else:
            print(" Please authenticate first by entering your PIN.")


    def deposit(self, amount):
        if   not self.is_authenticated:
            print(" Please authenticate first by entering your PIN.")
            return
        
        try:
            amount = float(amount)
            if amount < 0:
                print(" Invalid deposit amount. Please enter a positive value.")
            else:
                self.balance += amount
                print(f" Deposit successful! Your new balance is {self.balance} rupees.")
        except ValueError:
            print(" Invalid input. Please enter a valid amount.")



    def withdraw(self, amount):
        if  not self.is_authenticated:
            print(" Please authenticate first by entering your PIN.")
            return
        
        try:
            amount = float(amount)
            if amount < 0:
                print(" Invalid withdrawal amount. Please enter a positive value.")
            elif amount > self.balance:
                print(" Insufficient balance.")
            else:
                self.balance -= amount
                print(f" Withdrawal successful! Your new balance is {self.balance} rupees.")
        except ValueError:
            print(" Invalid input. Please enter a valid amount.")

    def exit(self):
        print(" Thank you for using the ATM.")

def main():
    atm = ATM()

    while True:
        print("\n **** Welcome to ATM **** ")
        
        if  not atm.is_authenticated:
            input_pin = input("Enter your PIN: ")
            try:
                input_pin = int(input_pin)
                atm.check_pin(input_pin)
            except ValueError:
                print("Invalid PIN format. Please enter a number.")

                break

        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = input("Enter amount to deposit: ")
            atm.deposit(amount)
        elif choice == "3":
            amount = input("Enter amount to withdraw: ")
            atm.withdraw(amount)
        elif choice == "4":
            atm.exit()
            break
        else:
            print(" Invalid choice. Please try again.")

# Call main() function!
main()