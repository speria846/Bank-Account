from datetime import datetime


class Account:
    def __init__(self,account_name,account_number):
        self.account_name=account_name
        self.account_number=account_number
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        self.transaction=100
        self.loan_balance=0
        self.new_account=0


    def deposit(self,amount):
        date=datetime.now()
        self.amount=amount
        if amount<=0:
            return f"hello customer deposit amount must be greater than zero(0)"
        else:
             self.balance+=amount
             dct={"date":date.strftime("%d/%m/%Y"),"amount":amount,"narration":f'thank you for depositing {amount} on {date}'}
             self.deposits.append(dct)
        return f"Hello {self.account_name} You have deposited Ugshs.{amount} and your new balance is {self.balance})"
       
   
    def withdraw (self,amount):
        self.amount=amount
        date=datetime.now()
       
        if amount>self.balance:
            return f"Hello customer,you have insuffient funds vafor making withdraw"
        elif amount<=0:
            return f"Hello customer, you can't withdraw  amount less than zero "            
        else:
             self.balance -=amount
             dct={"amount":amount,f'on'"date":date.strftime("%d/%m/%Y"),"narration":f'thank you for withdrawing'}
             self.withdrawals.append(dct)
        withdrawal_amount=self.balance-self.transaction
        if amount>withdrawal_amount:
            return "you have insufficient balance"
        self.balance-=amount+self.transaction
        return f"Yellow {self.account_name} ,you have withdrawn UGx.{amount} and your new balance is {self.balance} )"
                   
    def deposit_statement(self):
        for x in self.deposits:
            print (x)
    def withdraw_statement(self):
        for y in self.withdrawals:
            print(y)
         
    def current_balance(self):
        return f" hello Your current balance is  {self.balance}"
   
    def full_statement(self):
        statement=self.deposits+self.withdrawals
        for a in statement:
            print(a)    
    def borrow(self,amount):
        sum=0
        for y in self.deposits:
            sum+=y["amount"]
           
        if len(self.deposits) <10:
            return f"Hello customer you are not eligible to borrow.make {10-len(self.deposits)} to borrow "
        if amount<100:
            return f"Hello customer you are eligible to borrow atleast 100"  
        if amount>sum/3:
            return f"Hello customer you can only borrow upto {sum/3}"
        if self.balance!=0:
            return f"Hello you have Ugshs.{self.balance} you cant borrow yet you still have balance on your account"
        if self.loan_balance!=0:
            return f"Hello you have a debt of {self.loan_balance} you have to pay first for you to borrow."
        else:
            interest= 3/100*(amount)
            self.loan_balance+=amount+interest
            return f"Hello customer you have borrowed {amount} your loan is now at {self.loan_balance}"
   
    def loan_repayment(self,amount):
       
         if amount>self.loan_balance:
             self.balance+=amount-self.loan_balance
             self.loan_balance=0
             return f" Dear customer thank you for paying the loan of {amount-self.loan_balance} your account balance is {self.balance}"      
         else:
             self.loan_balance-=amount
             return f"thank you"
    def transfer(self,amount,new_account):
        if amount<=0:
            return "invalid amount"
        if amount>=self.balance:
            return f"insuficient funds"
        if isinstance(new_account,Account):
            self.balance-=amount
            new_account.balance+=amount
            return f"you have sent {amount} to  the new account with the name {new_account.account_name}.your new balance is {self.balance}"
  
         
             

        
    