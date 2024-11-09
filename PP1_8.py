
print(25 % 2)
print(2 % 25)
print(0 % 2)
print(24 % 2)
print(23 % 2)
print(1%2)

def q1():
  #Write Assignment code her
  bool1= 2 < 5
  bool2= 2 > 5
  print(bool1 and bool2)
  print(bool1 or bool2)

def q2():
  #Write Assignment code here
  num1 = int(input("Enter an integer: "))
  print(bool(num1))

def q3():
  #Write Assignment code here
  num2= input("Enter a number: ")
  num3= int(num2)
  print(bool(0 <= num3 <= 10))
  
def q4():
  #Write Assignment code here
  num4= input("Input food: ")
  num5= input("Input drink: ")
  print(bool(f"Your food and drink is {num4} != “pizza” and {num5} != "pop"))

def q5():
  #Write Assignment code here
  num6= input("Enter an integer: ")
  num7= int(num6)
  print(num7 % 2)
  bool8 = num7 % 2 == 0
  print(f"The integer {num7} is {bool8}")

#Do not edit code after this
#Comment out the followwing code when running tests

#q1()
#q2()
#q3()
#q4()
#q5()
