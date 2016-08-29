class Car(object):
  def __init__(self, price, speed, fuel, mileage,): #attributes: price, speed, fuel, mileage
    self.price = price
    self.speed = speed
    self.speed = fuel
    self.mileage = mileage
    self.tax = .12
    self.display_all =  #In the class have a method called display_all() that returns all the information about the car as a string. 
  
#If the price is greater than 10,000, set the tax to be 15%. 
#Otherwise, set the tax to be 12%. 
  def price():
    if price > 10000:
      self.tax == .15
  
    else: 
  
      self.tax == .12
    
    self.display_all() #In the class have a method called display_all() that returns all the information about the car as a string. 
  
  def display_all(self):
    print 'price: ' + str(self.price)
    print 'speed: ' + str(self.speed) + 'mph'
    print 'fuel: ' + self.fuel
    print 'mileage: ' + str(self.mileage) + 'mpg'
    print 'tax: ' + str(self.tax)

#Create six different instances of the class Car. 
car1 = Car(2000, 35, 'Full', 15)
car2 = Car(2000, 5, 'Not Full', 105)
car3 = Car(2000, 15, 'Kind of Full', 95)
car4 = Car(2000, 25, 'Full', 25)
car5 = Car(2000, 45, 'Empty', 25)
car6 = Car(20000000, 35, 'Empty', 15)