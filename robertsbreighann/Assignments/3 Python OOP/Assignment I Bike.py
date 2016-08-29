class Bike(object):
  def __init__(self, price, max_speed, miles):
    self.price = price
    self.max_speed = max_speed
    self.miles = 0
  
# have this method display the bike's price, maximum speed, and the total miles
  def displayInfo(self):
    print 'Price is: $' + str(self.price)
    print 'Maximum Speed: ' + str(self.max_speed) + 'mph'
    print 'Total Miles: ' + str(self.miles) + ' miles'

# have it display "Riding" on the screen and increase the total miles ridden by 10
  def driving(self):
    print 'Riding'
    self.miles += 10


# have it display "Reversing" on the screen and decrease the total miles ridden by 5
  def reverse(self):
    print 'Reversing'
    if self.miles >= 5
        self.miles -= 5

