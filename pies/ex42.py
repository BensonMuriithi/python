"""relationship between class, inheritance and objects"""
#forgive the misuse of a in place of an

#Animal is-a object
class Animal(object):
    def __init__(self, name):
        self.name = name
    
    def sound(self, s):
        print s + " " + s

#dog is a Animal
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
    def bark(self):
        super(Dog, self).sound("Woof!")
        

#Cat is a Animal
class Cat(Animal):
    #def __init__(self, name):
        #Cat has a name.
    #   self.name = name
    
    def meow(self):
        super(Cat, self).sound("Meow")

#Person is a object     
class Person(object):
    def __init__(self, name):
        #Person has a name
        self.name = name
        #Person has a pet
        self.pet = None
    def sing(self):
        print "\a\a\a\a\aThis is a melody.\a"
        
    
#Employee is a Person
class Employee(Person):
    def __init__(self, name, salary):
        """come back to this"""
        super(Employee, self).__init__(name)
        #Employee has a salary
        self.salary = salary

#Fish is a object
class Fish(object):pass

#Salmon is a fish
class Salmon(Fish):pass

#Halibut is a fish
class Halibut(Fish):pass

#rover is a dog
rover = Dog("Rover")
#satan is a cat
satan = Cat("Satan")
#mary is a person
mary = Person("Mary")
mary.pet = satan
#frank is an employee
frank = Employee("Frank", 120000)
frank.pet = rover

rover.bark()
satan.meow()
print rover.name
print satan.name