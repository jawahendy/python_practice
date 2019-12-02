# poly
class standup():
  def laugh(self):
    return "laugh() called"

  def __str__(self):
    return "your stand up very funny"

obj = standup()
print(obj)

# poly with exercise: must be same def in indonesia and malaysia
class Indonesia():
  def capital(self):
    print("jakarta is the capital of Indonesia.")

  def language(self):
    print("bahasa is the primary language.")
  
  def type(self):
    print("indo is beautifull country")

  def presiden(self):
    print("presiden in Indonesia is bpk Jokowi dodo")

class Malaysia():
  def capital(self):
    print("I dont know what is name")

  def language(self):
    print("bahasa melayu is the primary.")

  def type(self):
    print("malaysia is I dont know what to say")
  
  def presiden(self):
    print("in Malaysia have.......")

obj_ind = Indonesia()
obj_malay = Malaysia()

for country in (obj_ind, obj_malay):
    country.capital()
    country.language()
    country.type()
    country.presiden()

# poly with inheritance

class lamp:
  def turnon(self):
    print("lamp can trun on")

  def turnoff(self):
    print("lamp can turn off")

  def cantTurnon(self):
    print("lamp cant turn on")

class electriclamp(lamp):
  def turnon(self):
    print("electric lamp can turn on")

class pertomaxlamp(lamp):
  def cantTurnon(self):
    print("pertomax lamp cant trun on because oil is gone. ")

obj_lamp = lamp()
obj_elec = electriclamp()
obj_pert = pertomaxlamp()

obj_pert.cantTurnon()
obj_lamp.turnon()
obj_elec.turnon()

# poly with function

class woodendoor():
  def canopen(self):
    print("wooden door can open with key")

  def cantopen(self):
    print("wooden door cant open with key becuase wrong key")

class alumuniumdoor():
  def canopen(self):
    print("alumunium door can open with password key")

  def cantopen(self):
    print("alumunium door opened because this door wrong password")

def can(obj):           #this is function
  obj.canopen()
  obj.cantopen()

obj_wood = woodendoor()
obj_alum = alumuniumdoor()

can(obj_alum)
can(obj_wood)