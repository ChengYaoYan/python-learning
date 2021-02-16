# xyz = [i for i in range(5000000000000000000000000000000)]
# print(xyz)

# generator 无怎么占用内存，虽然在运行速度上有所牺牲
xyz = (i for i in range(5000000000000000000000000000000))
print(xyz)

for i in xyz:
    print(i)