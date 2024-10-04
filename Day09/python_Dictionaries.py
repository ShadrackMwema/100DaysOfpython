student_scores = {
    "shad": 80,
    "manu": 70,
    "Rolex": 54,
    "Rose": 76,
    "JOhn": 60,

}
# Structure of a dictionary

# name = {
#     key:value,
#     key:value,
# }


# Adding items to a dictionary
student_scores["emmanuel"] = 45
print(student_scores)

# Retrieving items from a dictionary
print(student_scores["emmanuel"])

#Printing an entire dictionary
student_scores["emmanuel"] = 30
print(student_scores["emmanuel"])

#Wipe an entire dictionary
# student_scores ={}
# print(student_scores)

#Looping through  a dictionary
for key in student_scores.keys():
    print(key)#print keys
    print(student_scores[key])#print values
