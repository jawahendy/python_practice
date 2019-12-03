# inheritance

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()


# exercise inheritance

class Kendaraan(object):

  def __init__(self, nama):
    self.nama = nama
    self.penumpang = []
    
  def tambah_penumpang(self, nama_penumpang):
    self.penumpang.append(nama_penumpang)
    
# membuat class Mobil yang merupakan turunan Kendaraan
class Mobil(Kendaraan):
  pintu_terbuka = False
  
  def buka_pintu(self):
    self.pintu_terbuka = True
  def tutup_pintu(self):
    self.pintu_terbuka = False
    
mobnas = Mobil("MobilSaya")

# mobnas akan memiliki properti dari Kendaraan
mobnas.tambah_penumpang("Raisa")
print ("Penumpang: " + str(mobnas.penumpang))
# dan memiliki properti Mobil
mobnas.buka_pintu()
print ("Pintu terbuka: " + str(mobnas.pintu_terbuka))


# exercise inheritance
class Bag(object):

  def __init__(self, nama):
    self.nama = nama
    self.jenis = []
    
  def tambah_Jenis(self, nama_jenis):
    self.jenis.append(nama_jenis)
class TasKulit(Bag):
  Tas_Open = False
  
  def open_bag(self):
    self.Tas_Open = True
  def close_bag(self):
    self.Tas_Open = False
    
bags = TasKulit("Tas Saya")
bags.tambah_Jenis("Skin")
print ("Tas jenis : " + str(bags.jenis))
bags.open_bag()
print ("Tas Opened : " + str(bags.Tas_Open))

# exercise inheritance

class Printer:
  def __init__(self, merk, serial):
    self.merk = merk
    self.serial = serial
  
  def merkprint(self):
    print(self.merk, self.serial)

name = Printer("canon", 2000)
name.merkprint()

class Ink(Printer):
  pass
ink = Ink("Hp", 1200)
ink.merkprint()

# exercise again
class Persons:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Students(Persons):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Students("Mike", "Olsen", 2019)
x.welcome()

# exercise again
class lamp:
  def __init__(self, color, watt):
    self.color = color
    self.watt = watt

  def printcategory(self):
    print(self.color, self.watt)

class gardenlamp(lamp):
  def __init__(self, color, watt, size):
    super().__init__(color, watt)
    self.size = size

  def category(self):
    print("this lamp have color ", self.color, self.watt," watt and size ", self.size)

lampu = gardenlamp("white", 20, "big and circle")
lampu.category()

# overriding 

import random
class Robot:
    
    def __init__(self, name):
        self.name = name
        self.health_level = random.random() 
        
    def say_hi(self):
        print("Hi, I am " + self.name)
        
    def needs_a_doctor(self):
        if self.health_level < 0.8:
            return True
        else:
            return False
        
class PhysicianRobot(Robot):
    def say_hi(self):
        print("Everything will be okay! ") 
        print(self.name + " takes care of you!")
    def heal(self, robo):
        robo.health_level = random.uniform(robo.health_level, 1)
        print(robo.name + " has been healed by " + self.name + "!")
doc = PhysicianRobot("Dr. Frankenstein")        
rob_list = []
for i in range(5):
    x = Robot("Marvin" + str(i))
    if x.needs_a_doctor():
        print("health_level of " + x.name + " before healing: ", x.health_level)
        doc.heal(x)
        print("health_level of " + x.name + " after healing: ", x.health_level)
    rob_list.append((x.name, x.health_level))
    
print(rob_list)

# little exercise overiding
import random
class Hero:
    
    def __init__(self, name):
        self.name = name
        self.Atk_level = random.random() 
        
    def say_hi(self):
        print("welcome to land of dawm, I am " + self.name)
        
    def needs_help(self):
        if self.Atk_level < 0.6:
            return True
        else:
            return False
class Magician(Hero):
    def say_hi(self):
        print("Everything will be okay! ") 
        print(self.name + " I will kill you!")
    def helping(self, heroes):
        heroes.Atk_level = random.uniform(heroes.Atk_level, 1)
        print(heroes.name + " has been Atk by " + self.name + "!")
doc = Magician("Dr. Frankenstein")
her_list = []
for i in range(5):
    x = Hero("Dracula" + str(i))
    if x.needs_help():
        print("atk_level of " + x.name + " before killing: ", x.Atk_level)
        doc.helping(x)
        print("Atk_level of " + x.name + " after Atking: ", x.Atk_level)
    her_list.append((x.name, x.Atk_level))
    
print(her_list)

# multiple inheritance

import random

class Robots():

    __illegal_names = {"Henry", "Oscar"}
    __crucial_health_level = 0.6
    
    def __init__(self, name):
        self.name = name  #---> property setter
        self.health_level = random.random()
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name in Robots.__illegal_names:
            self.__name = "Marvin"
        else:
            self.__name = name

    def __str__(self):
        return self.name + ", Robot"
 
    def __add__(self, other):
        first = self.name.split("-")[0]
        second = other.name.split("-")[0]
        return Robot(first + "-" + second)
    
    def needs_a_nurse(self):
        if self.health_level < Robots.__crucial_health_level:
            return True
        else:
            return False
 
    def say_hi(self):
        print("Hi, I am " + self.name)
        print("My health level is: " + str(self.health_level))

first_generation = (Robot("Marvin"),
                    Robot("Enigma-Alan"),
                    Robot("Charles-Henry"))
 
gen1 = first_generation # used as an abbreviation
babies = [gen1[0] + gen1[1], gen1[1] + gen1[2]]
babies.append(babies[0] + babies[1])
for baby in babies:
    baby.say_hi()

# multiple inheritance exercise

import random

class Personss():

    __names = {"Hendy", "Nurfrianto"}
    __health_level = 0.8
    
    def __init__(self, name):
        self.name = name  
        self.health_level = random.random()
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name in Personss.__names:
            self.__name = "Hendy"
        else:
            self.__name = name

    def __str__(self):
        return self.name + ", Doctor"
 
    def __add__(self, other):
        first = self.name.split("-")[0]
        second = other.name.split("-")[0]
        return Personss(first + "-" + second)
    
    def needs_a_nurse(self):
        if self.health_level < Personss.__health_level:
            return True
        else:
            return False
 
    def say(self):
        print("Hi, I am " + self.name)
        print("My health level is: " + str(self.health_level))
first_generation = (Personss("Hendy"),
                    Personss("Another Planet"),
                    Personss("Call me"))
 
gen1 = first_generation # used as an abbreviation
babies = [gen1[0] + gen1[1], gen1[1] + gen1[2]]
babies.append(babies[0] + babies[1])
for baby in babies:
    baby.say()

# multiple inheritance exercise


		
# definition of the class starts here  
class Person2:  
    #defining constructor  
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge  
  
    #defining class methods  
    def showName(self):  
        print(self.name)  
  
    def showAge(self):  
        print(self.age)  
  
    #end of class definition  
  
# defining another class  
class Student2: # Person is the  
    def __init__(self, studentId):  
        self.studentId = studentId  
  
    def getId(self):  
        return self.studentId  
  
  
class Resident(Person2, Student2): # extends both Person and Student class  
    def __init__(self, name, age, id):  
        Person2.__init__(self, name, age)  
        Student2.__init__(self, id)  
  
  
# Create an object of the subclass  
resident1 = Resident('John', 30, '102')  
resident1.showName()  
print(resident1.getId())  

# exercise 2

class coffe(object):
  def __init__(self, name):
    self.name = name

  def getname(self):
    return self.name
  
  def isgood(self):
    return False

class Latte(coffe):
  def __init__(self, name, pid):
    super(Latte, self).__init__(name)
    # or in python 3 can use this super 
    # super().__init__(name)
    self.prodID = pid

  def isgood(self):
    return True

  def getID(self):
    return self.prodID

prod = Latte("Latte Flower", "L01")
print(" name productnya : ",prod.getname()," ,product idnya : " ,prod.getID())

# exercise multiple inheritance
class html:
  def __init__(self):
    print("I'm in class Html yesterday")

  def person_html(self, a):
    print("person in class html: ", a)

class css(html):
  def __init__(self):
    print("I'm in class css now ")
    super().__init__()

  def person_css(self, a):
    print("person in class css :", a)
    super().person_html(a+1)

class javascript(css):
  def __init__(self):
    print("I'm in class javascript sesok")
    super().__init__()

  def person_js(self, a):
    print("person in javascript class :", a)
    super().person_css(a+1)

if __name__ == '__main__':

  course = javascript()
  course.person_js(20)

