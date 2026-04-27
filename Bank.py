class Bank:
    def __init__(self,acc,bal):
        self.account_holder=acc
        self.balance =bal
    
    def deposit(self,amt):
        self.balance +=amt
        print(f"Deposit success ")
        self.display_balance()

    def withdraw(self,amt):
        if amt< self.balance:
            self.balance-=amt
            print("Withdraw Success")
        else:
            print("insufficient balance")

    def display_balance(self):
        print(f"Current balance is : {self.balance}")


    


b1= Bank("gopesh",5000)
b2=Bank("rathinam",100)

b1.deposit(500)
b1.withdraw(1000)
b1.display_balance()
