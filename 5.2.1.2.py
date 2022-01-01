list = []
for a in range(0,10,1):
    list.append(int(input("Zahl: ")))
one = list[0]
for a in range(1,10,1):
    if one > list[a]:
        one = list[a]
two = list[0]
for a in range(1,10,1):
    if two < list[a]:
        two = list[a]
print(one,two)

