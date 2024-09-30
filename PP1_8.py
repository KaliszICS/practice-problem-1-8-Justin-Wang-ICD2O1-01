
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
  num = input("Enter an integer: ")
  bool = num == 0
  print("Your integer is: ", bool)

def q3():
  #Write Assignment code here
  num= input("Enter a number: ")
  num= int(num)
  bool = num > 0
  bool = num < 10
  print("Your number is: ",  num > 0 and num < 10)

def q4():
  #Write Assignment code here
  num= input("Input food: ")
  num1= input("Input drink: ")
  bool= num!="pizza"
  bool1= num1!="pop"
  print("Your food and drink is: ", bool and bool1)

def q5():
  #Write Assignment code here
  num= input("Enter an integer: ")
  num= int(num)
  print(num % 2)
  bool = num % 2 ==0
  print(f"The integer {num} is: ", bool)

#Do not edit code after this
#Comment out the followwing code when running tests

q1()
q2()
q3()
q4()
q5()
