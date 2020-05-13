sum = 0
count = 0
xStr = input()
while xStr != " ":
    x = int(xStr)
    sum = sum + x
    count = count+1
    xStr=input()
else:
    print(sum/count)
print("nihao")