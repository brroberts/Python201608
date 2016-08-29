class Animal(object):
    def __init__(self, name, health): #attributes: name, and health
        self.name = name
        self.health = 100 # new animal a health of 100 when it gets created

    def walk(self): #three methods: walk, run, and displayHealth
        self.health -= 1 # walk() method is invoked, have the health decrease by 1
        return self

    def run(self):  # run() method is involved, have the health decrease by 5
        self.health -= 5
        return self

    def displayHealth(self): # displayHealth() method is invoked, display on screen the name of the Animal and the health
        print "Animal Name: " + self.name
        print "With " + str(self.health) + 'health'

animal = Animal("Isabel") #Create an instance of the animal called 'animal' and have this animal walk three times, run twice, and displayHealth()
animal.walk().walk().walk().run().run().displayHealth()

#create another class called Dog that inherits everything that the Animal does 
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150 # have the default health be 150

    def pet(self): #add a new method called pet, which when invoked, increase the health by 5
        self.health += 5
        return self

dog = Dog("Cassie") #Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth()
dog.walk().walk().walk().run().run().pet().displayHealth()


class Dragon(Animal): #create another class called Dragon that also inherits everything from Animal
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170 #have the default health be 170

    def fly(self): #add a new method called fly, which when invoked, decreased the health by 10
        self.health -= 10
        return self

#When the Dragon's displayHealth function is called, have it say 'this is a dragon!' before it displays the default information (by calling the parent's displayHealth function).
    def displayHealth(self):
        print 'this is a dragon!'
        super(Dragon, self).displayHealth()

dragon = Dragon('Drogon') #Have the Dragon walk() three times, run() twice, fly() twice, and have it displayHealth()
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
