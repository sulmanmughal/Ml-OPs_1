from wallet import Wallet

def test_getAmount():
  obj = wallet()
  obj.setAmount(20)
  obj assert obj.getAmount == 20
