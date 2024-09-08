print("Welcome to POLOS HAMANOS PIZZA INN \n")
size =input("What size do you want? S,L,M\n")

add_pepperoni=input("Do you want Pepperoni?Y or N\n")
add_cheese=input("Do you want Cheese?Y or N\n")

S_price =15
M_price =20
L_price =25

S_pepperoni =2
M_pepperoni =3
L_pepperoni =3

extra_cheese =1

print(size)
if size == "S":
    pizzaPrice = S_price
    if add_pepperoni == "Y":
        pizzaPrice += S_pepperoni
    if add_cheese == "Y":
        pizzaPrice += extra_cheese
elif size == "L":
    pizzaPrice =L_price
    if add_pepperoni == "Y":
        pizzaPrice += L_pepperoni
        print(pizzaPrice)
    if add_cheese == "Y":
        pizzaPrice += extra_cheese
        print(pizzaPrice)
        print(extra_cheese)
else :
    pizzaPrice =M_price
    if add_pepperoni == "Y":
        pizzaPrice += M_pepperoni
        if add_cheese == "Y":
            pizzaPrice += extra_cheese


print(f"Your final bill is {pizzaPrice}")