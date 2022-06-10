class Account:
    def __init__(self,account_number,account_name): 
        self.account_name=account_name
        self.account_number=account_number
        self.balance=0
        self.deposits=[]
        self.withraw=[]
        self.transaction_fee=100
    
    def deposit(self,amount):
        if amount<=0:
            return f"deposit must be positive"
        else:
            self.balance+=amount
            # return f"hello{self.account_name} you have deposited {amount} and your new balance is {self.balance}"
            self.deposits.append(amount)
        return f"Hello, {self.account_name} you have deposited {amount} ,new balance is {self.balance}"

    def withraw(self,amount):
        total=amount+transaction_fee
        if amount<=0:
           return f"withdraw must be greater than this"
        elif amount>self.balance:
            print(f"your balance is {self.balance},you can't withdraw {amount}")
        else:
            self.balance-=total
            # return f"helo{self.account_name} you have withdrawn {amount} and your balance is {self.balance}"
            self.withraw.append(amount)
            return f"Hello, {self.account_name} you have deposited {amount} ,new balance is {self.balance}"
            
    def deposits_statement(self):
        for depo in self.deposits:
            print(depo,end="\n")

    def withraw_statement(self):
        for man in self.deposits:
            print(man,end="\n")

    def bal(self):
        print(f"your balance is {self.balance}")


# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which using a for loop prints each deposit in a new line
# Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance.