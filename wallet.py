class Wallet:
  def __init__(self, balance):
    self.balance = balance
    
  def setAmount(self, balance):
    self.balance = balance
    
  def getAmount(self):
    return self.balance
  
  def removeAmount(self, amount):
    self.balance = self.balance - amount
