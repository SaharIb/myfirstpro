# Read Mode 

'''myfile = open ("work.txt" , "r")
#print(myfile.read())
print (myfile.readlines())

print(myfile.read(5))
print(repr(myfile.read(15))) #'- Pythoon \nmari'   # The repr(s) function returns a raw string for s
print((myfile.read(15))) # - Pythoon
#mar
print (myfile.readline())
'''


# Write Mode

'''myfile = open ("work.txt" , "w") # Creat file if dont exist 
myfile.write ("Hello World in this text file new created\n")
myfile.write ( "Secound line in this text file new created\n")

mylist = ["Sahar\n" , "Mariam\n" , "Soma\n"]
myfile.writelines(mylist)'''

# Append mode 
'''
myfile = open ("work.txt" , "a")
myfile.write ("\nHello World in this text file new created\n")
myfile.write ( "Secound line in this text file new created\n")
myfile.write()'''

x  = int (input("Enter number 1 : "))
y  = int (input("Enter number 2 : "))
z  = int (input("Enter number 3 : "))
max = x 
if (y > max and y > z ):
    max = y
if (z > max ):
    max = z 
print(max)