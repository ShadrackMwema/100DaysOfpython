my_list =[]
bid_continue = True

while bid_continue ==True:
    bid = int(input("Enter your bid : "))

    if bid(i) not  in range(10):
        bid_continue = False


    my_list.append(bid)
    answer = input("Would you like to add another bid? (y/n) : ").lower()
    while  answer!='y' and answer!='n':
        answer = input("Invalid output? (y/n) : ").lower()
    if answer == "y":
        bid_continue = True
    elif answer == "n":
        bid_continue = False
