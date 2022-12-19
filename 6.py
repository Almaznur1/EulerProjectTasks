a = 0
for i in range(1,101):
	a = a + i ** 2
print(a)

b = 0
for i in range(1,101):
	b = b + i
b = b ** 2
print(b - a)