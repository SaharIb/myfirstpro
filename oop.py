class Student ():
    def __init__(self , name , final = 0 , mid = 0 ) :
        self._name = name
        self._final = final 
        self._mid = mid
    def setname (self , name):
        self._name = name
    def getname (self):
        return self._name
    def setfinal (self , final):
        self._final = final
    def getfinal (self):
        return self._final
    def setmid (self , mid):
        self._mid = mid
    def getmid (self):
        return self._mid

    def semster (self ):
        avg = ((self.getmid()+ self.getfinal())/2)
        if avg >=90 :
            return ("A")
        elif avg >=80 :
            return ("B")
        elif(avg >=70):
            return("C")
        else :return("F")
    def __str__(self) :
        return ("Name is : "+self.getname() + "\nThe Avg ="+str(self.semster()) )
    

    
std1 = Student ("Sahar" , 82 , 90)
print(std1)





