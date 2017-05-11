
class Orange():
    def __init__(self,w,c):
        self.weight=w
        self.color=c
        self.mold =0
        print("Created!")
        
    def rot(self, days, temp):
        self.mold=days*temp

orange=Orange(6,"Dark Orange")
print(orange.mold)
orange.weight=14
orange.rot(10,98)
print(orange.mold)
print(orange.weight)
