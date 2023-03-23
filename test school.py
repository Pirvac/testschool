from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self,name,age):
        return f"the person is called  {self.name} and he is {self.age} years old"

      
          

class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    

          


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def show_info(self):



teacher01 = Teacher("Adam", 39)
student01 = Student("Moad", 28)

show_info(teacher01)
show_info(student01)

        

