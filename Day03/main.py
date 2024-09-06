#Conditional statements
num= int(input("Enter a number: "))
if num > 10:
    print("Greater than 10")
else:
    print("Greater than or equal to 10")
# >=
# ==
# <=
# !=

#elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Nested if
  x = 41

  if x > 10:
      print("Above ten,")
      if x > 20:
          print("and also above 20!")
      else:
          print("but not above 20.")