# class A:
#  def __init__(self, x= 1):
#     self.x = x
# class der(A):
#     def __init__(self,y = 2):
#         super().__init__()
#         self.y = y
# def main():
#     obj = der()
#     print(obj.x, obj.y)
# main()

# class test:
#  def __init__(self,a):
#     self.a=a
#  def display(self):
#     print(self.a)
# obj=test(2)
# obj.display()



# def rareLetterCheck(testStr):
#  rareLetters = ['j', 'k', 'q', 'x', 'z']
#  for letter in testStr:
#     if letter in rareLetters:
#         return letter
# s = 'Quick brown fox'
# print(rareLetterCheck(s))

# 4.
# def reps(a, s, times):
#  frequent = []
#  for i in s:
#     if a.count(i) >= times:
#         frequent.append(i)
#  return frequent
# text = 'Make that cat go away! Tell that Cat in the Hat you do NOT want to play.'
# patterns = ['that', 'cat', 'ay']
# print(reps(text, patterns, 2))



# x = 'abcd'
# for i in range(len(x)):
#  z=x[i].upper()
#  print (z)




# l =  [3, 4, 5, 20, 5]
# # print(l*-2)
# print(l.index(5))

# myList = [1, 5, 5, 5, 5, 1]
# myList.append([1,2,3])
# print((myList))

# class A:
#  def __init__(self):
#     self.__i = 1
#     self.j = 5
#  def display(self):
#     print(self.__i, self.j)
# class B(A):
#  def __init__(self):
#     super().__init__()
#     self.__i = 2
#     self.j = 7 
# c = B()
# c.display()

# def f(x):
#     print("outer")
#     def f1(a):
#         print("inner")
#         print(a,x)
#     f1(1)
# f(3)

# x = 3
# def fun(b):
#    if b==0:
#       return b
#    return b+fun(b-1)
# def fun1(a):
#    return fun(a)+a

# def ff(a,b):
#    c= a+b+x
#    return fun1(c)

# print(ff(1,2))


s1 = str('python')
s2 = 'python'
print(s1==s2 , s1 is s2 , sep="*")