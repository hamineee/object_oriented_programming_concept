class Person:
    number_of_people = 0 # class attribute

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Tom")
print(Person.number_of_people)
p2 = Person("Jerry")
print(Person.number_of_people)
print(Person.number_of_people_())