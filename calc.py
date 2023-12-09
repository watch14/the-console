class Calcul():

    def __init__(self):
        while True:
            self.x = input("Choose your symbol (+ or - or * or /): ")
            if self.x in ["+", "-", "*", "/"]:
                print(f"You chose: {self.x}")
                break

        while True:
            try:
                self.a = int(input("Add First number (I only accept numbers): "))
                print("You entered:", self.a)
                break
            except ValueError:
                print("Please enter a Number.")

        while True:
            try:
                self.b = int(input("Add Second number (I only accept numbers): "))
                print("You entered:", self.b)
                break
            except ValueError:
                print("Please enter a Number.")

    def add(self):
        return self.a + self.b
    
    def mult(self):
        return self.a * self.b
    
    def minus(self):
        return self.a - self.b
    
    def div(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return

    def operation(self):
        if self.x == "+":
            print(f"{self.a} {self.x} {self.b} = {self.add()}")
        elif self.x == "-":
            print(f"{self.a} {self.x} {self.b} = {self.minus()}")
        elif self.x == "*":
            print(f"{self.a} {self.x} {self.b} = {self.mult()}")
        elif self.x == "/":
            result = self.div()
            print(f"{self.a} {self.x} {self.b} = {result}")

calculator = Calcul()
calculator.operation()
