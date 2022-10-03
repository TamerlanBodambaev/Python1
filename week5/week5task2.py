class S:
    
    def __init__(self, f="U", s="R"):
        self.f = f
        self.s = s

    def first_name(self):
        return (self.f.capitalize())

    def second_name(self):
        return (self.s.capitalize())

    def full_name(self):
        print (self.f.capitalize(), self.s.capitalize())
        return (self.f.capitalize(), self.s.capitalize())


a1 = S('john','SMITH')
print (a1.first_name())
print (a1.second_name())
print (a1.full_name())
