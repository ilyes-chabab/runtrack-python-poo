class operation:
    def __init__(self,nombre1,nombre2):
        self.nombre1=nombre1
        self.nombre2=nombre2
    def getnumber(self):
        print(f"le nombre1 est {self.nombre1}")
        print(f"le nombre2 est {self.nombre2}")
number=operation(12,3)
number.getnumber()