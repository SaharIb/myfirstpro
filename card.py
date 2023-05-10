# class Purchase:
       
#     def __init__(self ,description , price ,quantity  ) :
#         self.description = description
#         self.price = price
#         self.quantity = quantity
 
           
       
          
      
# class  Cart(Purchase):
#    def __init__(self , description , price ,quantity ):
#       super().__init__(description , price ,quantity )
      
# def info ():
#     list1 = []
#     s = 0
    
#     while True:
#         des = (input("Enter description of article: "))
#         pric =int(input("Enter price of article: ")) 
#         quant =int(input("Enter quantity of article: ")) 
#         list1.append([des , pric , quant])
#         s +=pric*quant
#         yorn = input("Do you want to enter more articles (Y/N)?")  
#         y = yorn.upper()
#         if (y == "N"):            
#             print("Article\t PRICE \t QUANTITY")
#             break
#     for row in list1:
#         for elemnt in row:
#             print(elemnt , end=" \t")
#         print() 
#     print(f"Total cost is : {s}")
# info()


# print(round(2.35,1))

# x = 0 
# print(x)
# def g ():
#     global x 


# # l1 = "Sahar"
# l1 = ["Sahar"]
# l2 = sorted(l1)
# l1.sort()
# print(l1)
# print(l2)

class Demo:
 def __init__(self):
       self.x = 1
 def change(self):
       self.x = 10
       return self.x
class Demo_derived(Demo):
       def change(self):
              self.x=self.x+1
              return self.x
def main():
       obj = Demo()
       print(obj.change())
main()
