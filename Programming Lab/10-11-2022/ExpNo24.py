str=input("Enter the String")
counts = dict()
str = str.split()

for i in str:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

print(counts)