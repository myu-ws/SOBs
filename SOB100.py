# 13 

print("Program to print star pattern: \n") 

number_of_rows = 5 

for y in range(0, number_of_rows + 1): 

    for x in range(0, y): 

        print("*", end='') 

    print () 

for y in range(number_of_rows, 0, -1): 

    for x in range(0, y-1): 

        print("*", end='') 

    print () 

 