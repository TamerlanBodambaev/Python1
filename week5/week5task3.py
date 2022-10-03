class Calculator:
    
    def __init__(self, f = 1, s = 1):
        self.f = f
        self.s = s

    def add (self):
        return self.f + self.s

    def sub (self):
        return self.f - self.s

    def mul (self):
        return self.f * self.s

    def div (self):
        return self.f / self.s
    
calculator = Calculator(10, 5)
print(calculator.add())
print(calculator.sub())
print(calculator.mul())
print(calculator.div())
