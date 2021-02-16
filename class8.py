x = [1, 3, 4]
y = [7, 6, 2, 1]
z = ['a', 'b', 'c', 'd', 'e']

# for a,b,c in zip(x,y,z):
##    print(a, b, c)

#[print(a, b, c) for a,b,c in zip(x, y, z)]


#[print(a, b) for a, b in zip(x, y)]
#print(a)


for a, b in zip(x, y):
    print(a, b)
print(a)
