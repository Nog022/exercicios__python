y,z,v,w = map(int, input().split()) #resto0 #resto+mais_que_zero #multiplo #não_multiplo 

var = -1
for x in range(2,100000):
    if x % y ==0 and  x % z!=0 and  v % x == 0 and v % x == 0 and w % x != 0:           
        
        var = x
        print(x)
        break
                           
if var != x:
    print(var) 
                    


                        