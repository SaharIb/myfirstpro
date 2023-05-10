'''y = 1
x  = 18 
area = 30 
print (f"tons of corn can be grown on a 30-acre farm is :  {(x*area/y)}")
''' 

'''v = 50 
h = 5
t =3
heightAfter_t_seconds = (-16*t**2 )+ v*t + h
print(heightAfter_t_seconds)'''

'''t1 = 5
t2 = 9 
t = t2-t1 
v = 81.34 *1000 / 3600
print(f"Distance covered is {v*t} m/s")'''

'''miles = 23352
miles_after = 23.695
gal = 14 
print (f"miles per gallon did the car average {miles_after/gal} gal/miles")'''

'''electricity = 750 * (10**6)
population = 5 * (10**6)
z = electricity/30
print(f"Dayly electricity  of one person is {z/population} 1pepole/day")'''

'''import math 
area = 432 
print (f"each side of the deck {math.sqrt(area)}")'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''n =float( input ("Enter number of seconds between lightning and thunder : "))
result = round( n/5 , 2 )
print ("Distance {:.2f}".format(result))


age = int(input(" Enter age "))
rest = int(input(" Enter resting heart rate "))
z = .7 * (220 - age) + .3 * rest
print(int(z))


n = input ("Enter name of team: ")
m = int (input ("Enter number of games won: "))
b = int (input ("Enter number of games lost: "))
res =( m / (m+b) ) *100
print(f"{n} won {res:.2f}% of their games.")


selling_price = float (input("Enter selling price: "))
purchase_price =float (input("Enter purchase price: "))
markup = float (input ("MarkeUp : "))
print(f"percentage_markup = {markup /purchase_price }%")
print (f"profit_margin = {markup / selling_price}%")

number =  (input ("Enter number floar : "))
z = str(number).find(".")
c = number[z:]
print (f" {c.count([z+1])}")
c1 = number[:z]
print(c1.count(c1))

sentence = input("Enter a sentence.")
word = input("Enter word to replace. ")
replacement = input("Enter replacement word. ")
start = sentence.find(word)
end = start + len(word)
print(sentence[0:start] + replacement + sentence[end : len(sentence)])

month =int (input("Enter a month : "))

y = month//12
m = month%12
print(f"{month} months is {y} years and {m} months") 

billAmount = float(input("Amount of Bill : "))
percent = float(input("Amount of Tip : "))
tip = billAmount * percent / 100
print(f" Tips : ${tip}")


n = float (input ("Enter revenue: "))
m = float (input ("Enter expenses: "))
z = n - m 
print (f"Net income: {z}")

sant = input("Enter a 3-part name: ")
mid = sant.split()[1]

print(mid)


sant = (input ("Enter float number : "))
dig = sant.split(".")
print(len(dig[0]))
print(len(dig[-1]))



'''
'''
salary=eval(input("Enter salary :"))
s=salary
new_Salary=salary*10/100
salary+=new_Salary
cut=salary*10/100
salary-=cut
print(salary)
s=(salary-s)/salary
print("change: ","{:.1%}".format(s))
'''
lst =[[]]*3
lst[0].append(5)
print(lst)
x,y=2,10 
x*=y*x+1
print(x)

print("abbcabcacabb".count('abb', 2, 11)) # 2 start 11 end

