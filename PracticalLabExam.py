scores = [26,49,98,87,62,75]
print(scores[1]+scores[3]+scores[5])
print(scores[0]+scores[2]+scores[4])
x = 0
y = 0
for sum in scores:
    if sum % 2 != 0:
        x +=sum
print(x)


for sum in scores:
    if sum % 2 == 0:
        y +=sum
print (y)

