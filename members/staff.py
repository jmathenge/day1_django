#from person import Person
import person

class Staff(person.Person):
    def __init__(self, first, last, role):
        super().__init__(first, last)
        self.role = role

    def __str__(self):
        return self.firstname+" "+self.lastname + " "+self.role



s = Staff("Allan", "T", "Computer Science Researcher")

print(s)
