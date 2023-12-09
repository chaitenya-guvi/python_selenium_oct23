"""
Multiple Inheritance

Python also allows classes to inherit from more than one parent class.
"""
class Aquatic:
  def __init__(self,name):
    self.name = name

  def swim(self):
    return f"{self.name} is swimming"

  def greet(self):
    return f"I am {self.name} of the sea!"

class Ambulatory:
  def __init__(self,name):
    self.name = name

  def walk(self):
    return f"{self.name} is walking"

  def greet(self):
    return f"I am {self.name} of the land!"

class Penguin(Aquatic,Ambulatory):
  def __init__(self,name):
    super().__init__(name=name)


jaws_aquatic = Aquatic("Jaws")
canine_ambulatory = Ambulatory("Canine")
captain_cook = Penguin("Captain Cook")


# """# 'Jaws is swimming'"""
# print(jaws_aquatic.swim())
# # jaws_aquatic.walk() # AttributeError: 'Aquatic' object has no attribute 'walk'
# """# 'I am Jaws of the sea!'"""
# print(jaws_aquatic.greet())
#
# canine_ambulatory.swim() # AttributeError: 'Ambulatory' object has no attribute 'swim'
# print(canine_ambulatory.walk())
# """# 'Lassie is walking'"""
# print(canine_ambulatory.greet())
# """# 'I am Lassie of the land!'"""
#


"""  Penguin inherits from both Aquatic and Ambulatory, 
therefore instances of Penguin can call both the walk and swim methods.
"""
print(captain_cook.swim())
"""# 'Captain Cook is swimming'"""
print(captain_cook.walk())
"""# 'Captain Cook is walking'"""
print(captain_cook.greet())
"""# 'I am Captain Cook of the sea!'"""
