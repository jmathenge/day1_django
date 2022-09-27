class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname  = last

    def __str__(self):
        return self.firstname+" "+self.lastname


p = Person("Allan", "Turing")

#print(p)


