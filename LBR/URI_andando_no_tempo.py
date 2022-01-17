x,y,z = map(int, input().split())

if x - y == 0 or x - z == 0 or y - x == 0 or y - z==0 or z - x==0 or z - y==0 :
    print('S')

elif ((x + y) - z == 0) or ((x + z) - y == 0) or ((y + x) - z == 0) or ((y + z) - x == 0) or ((z + x) - y == 0) or ((z + y) - x == 0):
    print('S')

else:
    print('N')