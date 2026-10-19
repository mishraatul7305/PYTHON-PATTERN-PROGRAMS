# right trianle 
n = 5
for i in range (n + 1):
    for j in range (n-1):
        print('', end='')
        
print('*' * i )      
    
        # left triangle 
def left_triangle(n=5):
    for i in range (n+1):
        for j in range(i):
            print('*',end='') 
            print(''* i)
            
    ------------#  hollow square========================================================== 
    
def hollow_square(n = 5):
    for i in range (n):
        if  i == 0 or i == 4 :
            j == 0 or j == 4;
            print('*', end ='')
        else:
            print('', end ='')
        print ('', end='')
                          
 # invert Right Triangle ----------------------------------------
 
def inverted_right_triangle(n = 5) :
    for i in range(n+1):
        for j in range(i):
            print('', end='')
        print('*' * (n=i))
            
                     