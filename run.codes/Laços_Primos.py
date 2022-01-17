A = int(input())
B = int(input())

for x in range(A,B+1):

    primo = True
    i = 2
    while primo and i < x:

        if x % i == 0:
            primo = False

        i += 1


    if primo and x != 1:
        print(x)

