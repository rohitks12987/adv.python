#method overrididng
class payment:
  def pay(self):
    pass
class UPI(payment):
  def pay(self):
    print("Pyment will be done by UPI")
class Cash(payment):
  def pay(self):
    print("payment done by cash")
class GooglePay(payment):
  def pay(self):
    print("payment will be done by GooglePlay")
p = [UPI(),Cash(),GooglePay()]   
for i in p:
  i.pay()