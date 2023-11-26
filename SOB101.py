# 2 

print("Program to print arrow pattern: \n") 

r = 5

for i in range(r, 0, -1): 

    print(" "*(r-i), "*")
 
for i in range(0, r+1, 1): 

    print(" "*(r-i), "*")
    
# 3

r = 5

def zigzag():
    for i in range(r, 0, -1): 

        print(" "*(r-i), "*")
    
    for i in range(0, r+1, 1): 

        print(" "*(r-i), "*")

for n in range(4):
    zigzag()



