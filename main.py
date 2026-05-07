import datetime


class Account:
    def __init__(self, customerId, customerName, balance, pin):
        self.__customerId = customerId
        self.__customerName = customerName
        self.__balance = balance
        self.__pin = pin
        self.__transactions = []
        self.__accountType = "Savings"
        self.__dailyLimit = 2000
        self.__lastWithdrawDate = None
        self.__dailyWithdrawAmount = 0

    # -----------------------Security--------------------#

    def verifyPin(self, pin):
        return self.__pin == pin

    # This is a function with an argument and return value. This basically telling that a stored pin is equal it entered pin. If it is equal then it will return true otherwise False.

    def changePin(self, oldPin, newPin):
        if self.verifyPin(oldPin):  # It will check whether the old pin is correct
            self.__pin = newPin
            print("PIN Updated Successfully!!")
        else:
            print("Invalid old PIN")

    # -------------------Basic Operations-----------------------------#

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid Deposit Amount")
        else:
            self.__balance = self.__balance + amount
            self.addTransactions("Depoit", amount)  # Here addTransaction is a method
        print(f"{amount} deposited successfully!")

    def withdraw(self, amount):
        today = datetime.date.today()

        if self.__lastWithdrawDate != today:
            # The above line means that the lastWithdrawDate is different from today's date so condition become true. So the new day is started.

            self.__dailyWithdrawAmount = 0
            self.__lastWithdrawDate = today

        if amount > self.__dailyLimit:
            # -> This above line means that Is user is trying to withdraw more than allowed limit in one transaction?
            print("Exceeds single transaction limit")
            return  # Here return is used to immedieatly stop the function after printing

        if (self.__dailyWithdrawAmount + amount) > self.__dailyLimit:
            print("Daily withdrawal limit exceeded")
            return

        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            self.__dailyWithdrawAmount = self.__dailyWithdrawAmount + amount
            self.addTransactions("Withdraw", amount)
            # Here addTransaction is a method for the tracsactions perfromed
            print(f"{amount} withdraw successfully")
        else:
            print("Insuffiecient Balance")

    def checkBalance(self):
        print(f"Current Balance : Rs.{self.__balance}")

    # -----------------------Transactions--------------------------#

    def addTransactions(self, txnType, amount):
        txn = {
            "type ": txnType,
            "amount": amount,
            "date": str(datetime.datetime.now()),
        }  # This will create a dictanory

        self.__transactions.append(txn)  # Add this transaction dictonary into the list

    def showTransactions(self):  # This will show all the saved transactions
        print("Transaction History: ")
        for txn in self.__transactions:
            # This will take transactions one by one from the list and print them
            print(txn)

    # ----------------Transfer from one account to another----------------#

    def transfer(self, targetAcc, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            targetAcc.__balance = targetAcc + amount

            self.addTransactions("Transer Out", amount)
            targetAcc.addTransactions("Transfer IN", amount)

            print(f"Transfered amount {amount} to {targetAcc.__cutomerName}")
        else:
            print("Insufficient Balance")

        # -----------------------Interest Payment-------------------#

    def intrest(self, rate=5):
        interest = (self.__balance * rate) / 100
        self.__balance = self.__balance + interest

        self.addTransactions("Interset ", interest)
        print(f"Interest of Rs. {interest} applied")
        print("--------Interest is added to you balance--------")

    # ------------------------Account Information--------------------#

    def accountInfo(self):
        print("-------Account Details-------")
        print("ID: ", self.__customerId)
        print("Name: ", self.__customerName)
        print("Type: ", self.__accountType)
        print("Balance: ", self.__balance)

    # -----------------Bank Statement---------------------------#


class BankSystem:
    def __init__(self):
        self.accounts = {}  # Empty dictonary

    # Creating an account here
    def createAcc(self):
        cid = input("Enter Customer ID: ")
        name = input("Enter Customer Name: ")
        balance = float(input("Enter Initail Balance: "))
        pin = input("Set PIN: ")

        acc = Account(cid, name, balance, pin)
        # Here we create an object by using the class

        self.accounts[cid] = acc

    def login(self):
        cid = input("Enter Cutomer ID: ")
        pin = input("Enter PIN:")

        acc = self.accounts.get(cid)

        if acc and acc.verifyPin(pin):
            print("-----Login Successfully!----")
            self.menu(acc)
        else:
            print("Invalid Credentials")

    def menu(self, acc):
        while True:  # This line keep running the code again and again
            print("1.Deposit  2.Withdraw 3.Balance 4.Transfer ")
            print("5.Transactions 6.Interest ")
            print("7.Change PIN 8.Exit ")

            choice = input("Enter Choice: ")

            if choice == "1":
                amnt = float(input("Amount: "))
                acc.deposit(amnt)

            elif choice == "2":
                amnt = float(input("Withdraw Amount: "))
                acc.withdraw(amnt)

            elif choice == "3":
                acc.checkBalance()

            elif choice == "4":
                anotherAcc = input("Transfer ID: ")
                amnt = float(input("Amount: "))
                target = self.accounts.get(anotherAcc)
                if target:
                    acc.transfer(target, amnt)
                else:
                    print("Another Account is not found to transfer")
            elif choice == "5":
                acc.showTransactions()

            elif choice == "6":
                acc.intrest()

            elif choice == "7":
                old = input("Input Old PIN: ")
                new = input("Input New PIN")

                acc.changePin(old, new)
            elif choice == "8":
                break
            else:
                print("Invalid Choice")

    # -------------Main System------------#


bank = BankSystem()

while True:
    print("\n--- BANK SYSTEM ---")
    print("1.Create Account")
    print("2.Login")
    print("0.Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        bank.createAcc()
    elif ch == "2":
        bank.login()
    elif ch == "0":
        break
    else:
        print("Invalid Choice")
