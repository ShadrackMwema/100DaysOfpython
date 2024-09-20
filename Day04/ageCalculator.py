from datetime import datetime
print("Welcome to the ultimate age calculator")
names = input("Please enter names separated by a comma")
names = names.split(',')
years = input("Please enter years separated by a comma")
years = years.split(',')
current_year = datetime.now().year

for i  in range(len(names)):
    name = names[i]
    year = current_year - int(years[i])
    print(f"{name} is {year} years old")
