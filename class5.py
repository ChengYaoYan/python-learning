input_list = [5, 6, 2, 10, 15, 20, 5, 2, 1, 3]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


xyz = (i for i in input_list if div_by_five(i))
##xyz = []
##for i in input_list:
##    if div_by_five(i):
##        xyz.append(i)
#[print(i) for i in xyz]

xyz = [i for i in input_list if div_by_five(i)]
# print(xyz)


# [[print(i, ii) for ii in range(5)] for i in range(5)]
#for i in range(5):
#    for ii in range(5):
#        print(i, ii)

xyz = (([i, ii] for ii in range(5) for i in range(5)))
#print(xyz)
#print([i for i in xyz])


xyz = (print(i) for i in range(5))

for i in xyz:
    i