x = 3
y = 2
z = 2
s = 0

for i in range(50):
    s = s + (x/(y**z))
    x = x + 3
    y = y *2
    z = z + 1
print('soma=',s)