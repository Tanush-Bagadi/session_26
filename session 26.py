from datetime import date
class Person:
    def __init__(self,name,age) :
        self.name = name
        self.age = age 
    @classmethod
    def birthyear(cls,name,year):
        return cls(name,date.today().year - year)

    @staticmethod
    def isadult(age) :
            return age>18

p1 = Person("pavie",18)
p2 = Person.birthyear("Ananya",2010)

print(p1.age)
print(p2.age)
print(Person.isadult(17))
