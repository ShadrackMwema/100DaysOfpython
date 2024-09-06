name=input("Enter your name: ")


height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

height = float(height)
weight = float(weight)

#rounding to 3 decimal places:
MBI=(round(weight/(height*height),2))

#Floor division
print(8//2)

#f-STRING
print(f"Hello{name}yOUR BMI is {MBI}")