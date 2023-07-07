n = 5

for i in range(1, n+1):
    side = " "*(n-i)
    print(side+"* "*i)
for i in range(1, n+1):
    side = " "*(i)
    print(side+"* "*(n-i))
