#َQ33
'''pound = eval(input ("Enter weight in pounds: "))
payment = eval(input ("Enter payment in dollars: "))

z = pound*2.50
change = payment - z 
print(f"Your Change is ${change : .2f} . ")'''

#َQ34

'''current = eval (input("Enter current balance: " ))
withdrawal = eval (input("Enter amount of withdrawal: "))
new_balance = current - withdrawal
if (withdrawal > current):
    print("“Withdrawal denied.”")
elif (new_balance < 150):
    print("“Balance below $150”")
else : 
    print (f"The new balance is $ {new_balance : .2f} .")
'''
#َQ35

'''
upper = input ("Enter a single uppercase letter: ")

if (len(upper)>1):
    print("You did not comply with the request.")
else : print ("You comply with the request")'''
#َQ36


'''year = int(input("Enter a Year : "))
if ((year%4 ==0) and (year%100 !=0)):
    print (f"{year} is a leap year . ")
else : print (f"{year} isn't a leap year . ")'''

#َQ42

'''first = eval(input("Enter cost of first suit: "))
secound = eval(input("Enter cost of secound suit: "))
cal = first*50/100 + secound 
print (f"Cost of the two suits is ${cal:.2f}")'''

#َQ43

'''income = eval (input ("Enter your taxable income:"))
tax = 0 
if (income <= 20000):
    tax = int(0.02*income)
    print(f"your tax is $ {tax:,}")
elif (income <= 50000):
    tax =int (400+0.025 * (income-20000))
    print(f"your tax is $ {tax:,}")
else :
    tax =int(1150 + .035 *(income - 50000))
    print(f"your tax is $ {tax:,}")
'''
#َQ19

'''now_year =  1980
your_barth =int( input ("Enter your B.D : "))
age=int( input ("Enter your age : "))
x =age**2- (now_year - your_barth)

print (f"Person will be {age} in the year {x}.")    
'''

#َQ20

'''pop = 7
year = 2011
while pop<8:
    pop+= pop*0.011
    year+=1

print (f"World population will be 8 billion in the year {year}.")
'''
# Q 31
'''
balance = 1000 
print("Options: \n1. Make a Deposit \n2. Make a Withdrawal \n3. Obtain Balance \n4. Quit")

while True :
    option =int (input("Make a selection from the options menu: "))

    if option ==1 :
        deposit =eval (input ("Enter amount of deposit: "))
        balance += deposit
        print("Deposit Processed.")
    if option ==2 :
        while True :

            withdrawal =eval(input("Enter amount of withdrawal: "))
            if withdrawal <= balance :
                print("Withdrawal Processed.")
                balance -= withdrawal
                break
            elif withdrawal > balance :
                print (f"Denied. Maximum withdrawal is ${balance : .2f}")
    if option == 3 : 
        print (f"Balance : ${balance}")
    if option ==4 :
        break 
        
'''

#َQ66

'''
n = int(input("How many numbers do you want to enter? "))
number = []

for i in range(n):
    Input_num = float(input("Enter a measurement: "))
    number.append(Input_num)
if n % 2 == 0:
    median = (number[int(n/2)-1] + number[int(n/2)]) / 2
else:
    median = number[int(n/2)]

print("The median is:", median)
         
'''
#َQ71

'''
infile = open ("mark.txt")
mark = []
count = 0 
for i in infile:
    markInt = float(i.strip())
    mark.append(markInt)
numGrade = len(mark)
avgGrade = sum (mark) / numGrade
print(f"Number of Grade :{numGrade} "  )
print(f"Avg of Grade : {avgGrade : .2f}" )

above_mark = []
for marks in mark :
    if marks > avgGrade :
        above_mark.append(marks)
perMark = (len(above_mark)/numGrade)*100
print(f"Percentage of grades above average: {perMark :.2f}%")
'''
#َQ72

'''
grades = []
for i in range(5):
    grade = float(input("Enter grade: "))
    grades.append(grade)
grades = grades[2:]
avg_grade = sum(grades) / len(grades)
print(f"Average grade after dropping two lowest grades: {avg_grade:.2f}")
'''
#َQ73

'''
vowel = ["a" , "e"  , "o" , "i" ,"u"]
num_vowel = []
word = input ("Enter a word : ")
for i in word :
    if (i in vowel ) and (i not in num_vowel) :
        num_vowel.append(i)
print(f"Number of different vowels:{ len(num_vowel)}" )
'''
#َQ25

'''
def find_max (number):
    max_num = number[0]
    for i in number :
        if i > max_num : 
            max_num = i 
    return max_num 
nums =[20 , 19 , 51 ]
print (find_max(nums) )
            
'''
#َQ26


'''
def word (string , substring ):
    count = 0
    i = 0
    while i < len(string) :
        if string[i:i+len(substring)] == substring :
            count+=1
            i+= len(substring)
        else : i+=1 
    return count 

print(word ("saharrr" , "r"))
'''
#َQ28

'''
def fact (n):
    x = 1
    for i in range (1, n+1):
        x = x * i   
    return x  

postive_num = int (input("Enter positive number : "))
if (postive_num > 0):
    num = fact(postive_num)
    print(num)
else: 
    print ("Enter just positive number please")

'''
#َQ50

'''
import math
def semeGarde (mid , final ):
    avg = (mid + 2*final)/3
    avg = math.ceil(avg)
    if (avg >=90):return ("A")
    elif (avg >=80):return ("B")
    elif (avg >=70):return ("C")
    elif (avg >=60):return ("D")
    else :print ("F")
mid = int (input("Enter midTerm :"))
final = int (input("Enter Final Exam  :"))
Grade = semeGarde (mid , final)
print (f"Semester Grade: {Grade}")
'''
#َQ59


'''import math

def largestPrimeFactor(n):
    maxPrime = 1
    
    while n % 2 == 0:
        maxPrime = 2
        n /= 2
    
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            maxPrime = i
            n /= i
    
    if n > 2:
        maxPrime = n
    
    return maxPrime

numbers = [21, 49, 55, 77, 91, 105, 121, 143]

sortedNumbers = sorted(numbers, key=largestPrimeFactor)

print("Numbers sorted by largest prime factor:", sortedNumbers)
'''
#َQ60

'''
numbers = [25, 14, 37, 46, 89, 63, 52, 71]

def lastDigit(n):
    return n % 10

sortedNumbers = sorted(numbers, key=lastDigit, reverse=True)

print("Numbers sorted by last digit:", sortedNumbers)
'''

print ("H.B.D")
