a = 6
i = 2
arr = []
print(range(2,a))
for i in range(2,a):
	if a % i == 0:
		arr.append(i)
print(arr)