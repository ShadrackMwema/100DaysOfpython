travel_log =[
    {
        "country":"France",
        "visits":12,
        "cities":["Paris","little","Dijon"]

    },
    {
        "country":"Germany",
        "visits":5,
        "cities":["Berlin","Hamburg","Stuttgart"]

    },

]

my_dictionary={}
def add_new_country(country,visits,cities):
    my_dictionary["country"]=country,
    my_dictionary["visits"]=visits,
    my_dictionary["cities"]=cities



add_new_country("Russia",2,["Moscow","Saint p"])
travel_log.append(my_dictionary)
print(travel_log[-1])