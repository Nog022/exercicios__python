x = []
for i in range(10):
    x.append(int(input()))
    if x[i] == 0 or x[i] < 0:
        x[i] = 1 
    
    print('X[{}] = {}'.format(i,x[i]))
