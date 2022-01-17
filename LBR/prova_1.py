car0,mot0,car1,mot1 = map(int, input().split())
car2,mot2,car3,mot3 = map(int, input().split())

if car0 <= car2 <= car1 or car0 <= car3 <= car1:
    print(1)
else:
    print(0)


