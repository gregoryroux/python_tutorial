# Read the data file
#filename = "data/wxobs20170821.txt"
#datafile = open(filename, 'r')
#print(datafile.readline())
#data = datafile.read()

data=[]
#with open(filename, 'r') as datafile:
#   data = datafile.read()

# Read and parse the data file
filename = "data/wxobs20170821.txt"
with open(filename, 'r') as datafile:

 # Read the first three lines (header)
 for _ in range(3):
    datafile.readline()

 # Read and parse the rest of the file
 for line in datafile:
    datum = line.split()
    data.append(datum)

# DEBUG
#for datum in data:
#   print(datum)
# DEBUG
#print(data[0])
print(data[8])
#print(data[-1])
#for datum in data[0:10]:
#    print(datum)

print(data[8][4])
print(data[8][:5])
print(data[8][::2])

# DEBUG
#print(data)
#print(type(data))

