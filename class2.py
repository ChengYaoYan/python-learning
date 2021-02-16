names = ['Jeff', 'Gary', 'Jill', 'Samantha']

# for name in names:
#     print('Hello there, ' + name)
#     print(' '.join(['Hello there,', name]))

# print(', '.join(names))

# import os
# 
# location_of_file = '/home/cyy/Workspace/Python/object-oriented-programming'
# file_name = 'example.txt'
# 
# with open(os.path.join(location_of_file, file_name)) as f:
#     print(f.read())

who = 'Gary'
how_many = 12

# Gary bought 12 apples today

print(who, 'bought', how_many, 'apples today!')
print('{} bought {} apples today!'.format(who, how_many))