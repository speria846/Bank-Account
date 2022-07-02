from datetime import datetime
from ntpath import join
class Account:
    def __init__(self,account_name,account_number):
        self.account_number=account_number
        self.account_name=account_name
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        self.transaction=100
        self.loan_balance=0
       
   
    def withdraw (self,amount):
        self.amount=amount
        date=datetime.now()
       
        if amount>self.balance:
            return f"Dear customer, you have insuffient funds for this withdraw"
        elif amount<=0:
            return f"Dear customer, you can't withdraw zero amount "            
        else:
             self.balance -=amount
             dct={"date":date.strftime("%d/%m/%Y"),"amount":amount,"narration":f'thank you for withdrawing at { date} '}
             self.withdrawals.append(dct)
        withdrawal_amount=self.balance-self.transaction
        if amount>withdrawal_amount:
            return "insufficient balance"
        self.balance-=amount+self.transaction
        return f"You have withdrawn Ugshs.{amount} and your new balance is {self.balance} on {date.strftime('%d/%m/%Y')})"
             
     
    def deposit(self,amount):
        date=datetime.now()
       
        self.amount=amount
        if amount<=0:
            return f"deposit amount must be greater than zero(0)"
        else:
             self.balance+=amount
             dct={"date":date.strftime("%d/%m/%Y"),"amount":amount,"narration":f'thank you for depositing at { date}'}
             self.deposits.append(dct)
             
        return f"You have deposited Ugshs.{amount} and your new balance is {self.balance} on {date.strftime('%d/%m/%Y')})"
   
         
    def deposit_statement(self):
        for x in self.deposits:
            print (x)
    def withdraw_statement(self):
        for y in self.withdrawals:
            print(y)
         
    def current_balance(self):
        return f" Your current balance is  {self.balance}"
   
    def full_statement(self):
        statement=self.deposits+self.withdrawals
        for a in statement:
            statement.sort(key=lambda a:a['date'],reverse=True)
            date=a['date']
            naration=a['narration']
            amount=a['amount']
            print(f"{date} '------' {naration} '-------'  {amount}")    
    def borrow(self,amount):
        sum=0
        for y in self.deposits:
            sum+=y["amount"]
           
        if len(self.deposits) <10:
            return f"you are not eligible to borrow.make {10-len(self.deposits)} to borrow "
        elif amount<100:
            return f"you can borrow atleast 100"  
        elif amount>sum/3:
            return f"you can borrow upto {sum/3}"
        elif self.balance!=0:
            return f"you have Ugshs.{self.balance} you cant borrow any money because you still have balance of {self.balance} on your account"
        elif self.loan_balance!=0:
            return f"you have a unpaid debt of {self.loan_balance} you have to pay first for you to borrow money."
        else:
            interest= 3/100*(amount)
            self.loan_balance+=amount+interest
            self.balance+=amount
            return f"you have borrowed {amount} your new loan is now at {self.loan_balance}"
   
    def loan_repayment(self,amount):
       
         if amount>self.loan_balance:
             self.balance+=amount-self.loan_balance
             self.loan_balance=0
             return f" thank you for paying the loan of {amount-self.loan_balance} your account balance is {self.balance}"
               
         else:
             self.loan_balance-=amount
             return f"thank you, and your debt balance remains {self.loan_balance}"
           
         
    def transfer(self,amount,account):
        if amount<self.balance:
           self.balance-=amount
           account.deposit(amount)
           return f"you have sent {amount} to the account with the name {account.account_name}.your new balance is {self.balance}"
        else:
           amount>self.balance
           return {f"you have insuffient funds on your {account}"}
  
             

        
    