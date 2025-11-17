class BankAccount:
  def __init__(self, owner, balance = 0):
    self.owner= owner
    self.balance = balance
    
  def deposit(self, amount):
    self.balance+=amount
    
  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance-=amount 
    else:
      print("Insufficient funds")
  
  def get_balance(self):
    return self.balance
  
# Object 
account = BankAccount('Minjo', 250) 
print(account.owner, account.balance)
account.deposit(100)
account.withdraw(50)     
print('Balance: ', account.get_balance())  