# 2 

print("Program to print arrow pattern: \n") 

r = 4

for i in range(r, 0, -1): 

    print(" "*(r-i), "*")
 
for i in range(0, r+1, 1): 

    print(" "*(r-i), "*")

# 2

print("\n")

star_list = ["*"] * 10 # ['*','*',....]
r = len(star_list)-1 # 10

i = 0
while i < r:
    if i < 5:
        print(" "*(i), star_list[i] )
    else:
        print(" "*(r-i-1), star_list[i])
    i+=1
    
# 3

print("\n")

def zigzag():

    star_list = ["*"] * 10 # ['*','*',....]
    r = len(star_list)-1 # 10

    i = 0
    while i < r:
        if i < 5:
            print(" "*(i), star_list[i] )
        else:
            print(" "*(r-i-1), star_list[i])
        i+=1

for n in range(3):
    zigzag()