import struct
import array

filename = "40mmcube.stl"

binlist = []

bytes_wanted = 150

with open(filename, "rb") as file:
	# remove 80 char header
	print(file.read(80))

	# read num of triangles
	test = struct.unpack('I', file.read(4))
	binlist.append(test[0])

	num_triangles = test[0]

	for i in range(1, num_triangles+1):
		bin = struct.unpack('12f', file.read(48))
		attr = struct.unpack('h', file.read(2))

		for item in bin:
			item = round(item, 3)
			str_bin = str(item)
			binlist.append(str_bin)
	
print(binlist)

print("Number of triangles:", binlist[0])

count = 1

for i in range(1, len(binlist), 12):
	print("Triangle #", count)
	count += 1
	print("Normal vector:", binlist[i:i+3])
	print("Vertex 1:", binlist[i+3:i+6])
	print("Vertex 2:", binlist[i+6:i+9])
	print("Vertex 3:", binlist[i+9:i+12])


my_dict = {}

for thing in binlist:
	if thing not in my_dict:
		my_dict[thing] = 1
	else:
		my_dict[thing] += 1

print(my_dict)