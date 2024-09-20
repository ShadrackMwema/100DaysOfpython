heights =input("please enter heights separated by a comma: ").split(',')
print(heights)

# total = 0
# for height in heights:
#     total += int(height)
# print(total)
# average = round(total/len(heights))
# print(f"the average of {heights}  is {average}")

total = 0
for h in range(len(heights)):
    total += int(heights[h])
print(total)
print(total/len(heights))
