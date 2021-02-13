class Person:
    def __init__(self,param_name):
        print("i am created!", self)
        self.name = param_name
    def talk(self):
        print("hi my name is", self.name, "nice to meet you")

person_1 = Person("alice") #constructor
print(person_1.name)
person_1.talk()
print(person_1)
person_2 = Person("johnny")
print(person_2)