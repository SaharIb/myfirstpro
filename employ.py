# # s ="sahar"
# # [print (list(x)) for x in s]
# # inds = [x*2 for x in s if s[0]=="s"]
# # print(inds)

# # z = 0 
# # def tra ():
# #     global z 
# #     z +=5
# #     print (z)
# # print(z)
# # tra()
# # print(z)

# # x = lambda a , b:a*10 + b*2
# # print(x(2,3))

# class World:
#        def hello(self, name=None):
#               if name is not None:
#                    print ("Hello", name)
#               else:
#                    print("Hello")
# obj = World ()       # calling function without any argument
# obj.hello("ssss") # calling function with an argument.


class Std:
    def __init__(self , name = "" , mid = 0 , final = 0) :
        self.name = name
        self.mid = mid
        self.final = final
    def calcGrade(self):
        average = int(self.mid + self.final)/2
        average = round(average)
        if average >=90:
            return "A"
        elif average >=80:
            return "B"
        elif average >=70:
            return "C"
        elif average >=60:
            return "D"
        else:
            return "F"
    def __str__(self) :
        return self.name +"\t" + self.calcGrade()
class gstd (Std):
    def __init__(self, name="", mid=0, final=0):
        super().__init__(name, mid, final)
        self.name = name
        self.mid = mid
        self.final = final
    def calcGrade(self):
        average = int(self.mid + self.final)/2

        average = round(average)
        if average >=60:
            return "Pass"
        else:
            return "Fail"        
        
def main ():
     name = input ("Enter your name : ")
     mid = input ("Enter MidTerm : ")
     final = input ("Enter Final Exam : ")
     std1 = Std (name , mid , final)
     std2 = gstd(name , mid , final)
     s = std2.calcGrade()
     print(std1)
     print(s)
main()

 
