class Animal:
    def __init__(self,name,tail,breed,legs):
        self.name=name
        self.tail=int(tail)
        self.breed=breed
        self.legs=int(legs)

    def __str__(self) -> str:
        return '{} {} {} {}'.format(self.name,self.tail,self.breed,self.legs)

    def triangle(n):
        for i in range(1,n+1):
            print()
            for j in range(1,i+1):
                print(j,end=' ')
            


e1=Animal('Murka',1,'Schips',4)
e2=Animal('Aktos',1,'Alabai',4)


 



Animal.triangle(5)