# Read the data file
filename = "data/wxobs20170821.txt"
#datafile = open(filename, 'r')
#print(datafile.readline())
#data = datafile.read()

with open(filename, 'r') as datafile:
   data = datafile.read()

# DEBUG
print(data)
print(type(data))

