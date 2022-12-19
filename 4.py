arr = []
for i in range(500,1000):
	for a in range(500,1000):
		b = a * i
		c = str(b)
		if (c[0] == c[5]) and (c[1] == c[4]) and (c[2] == c[3]):
			arr.append(b)
print(max(arr))
