class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def afficherLesPoints(self):
        print(f"coordonnées : ({self.x} , {self.y})")
    def afficherX(self):
        print(f"x={self.x}")
    def afficherY(self):
        print(f"y={self.y}")
    def changerX(self,x):
        self.x = x
    def changerY(self,y):
        self.y = y
coordoonnées=point(200,600)
coordoonnées.changerX(400)
coordoonnées.changerY(1200)
coordoonnées.afficherX()
coordoonnées.afficherY()
coordoonnées.afficherLesPoints()

        