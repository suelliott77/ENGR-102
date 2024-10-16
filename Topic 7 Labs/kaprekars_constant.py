    # By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
# Section:      504
# Assignment:   Indivdual lab 7d
# Date:         12 October 2022

integer= input("Enter a four-digit integer: \n")
constant=0
list_int= []
iterations=0
list_new= []
differ=0

#split up the number entered 
for i in range(len(integer)):
    list_int.append((integer[i]))

#added a zero if the entered number has 1-3 digits 
for i in range(4-(len(integer))):
    list_int.append('0')
              
print(integer, end=" > ")

while constant != 6174:
#sort to get the lower number
    list_int.sort()
    low= int("".join(list_int))
#reverse to get the higher number
    list_int.reverse()
    high= int("".join(list_int))
#find the difference
    differ= (high - low)
    iterations+=1
       
#difference print 
    if differ == 0:
        print(f"0 \n{integer} reaches 0 via Kaprekar's routine in 1 iterations")
        break
    else:
        
        if differ != 6174:
            print(differ, " > ", end= "")
        
            constant=differ
        
            list_int= str(differ)
            list_int=[i for a, i in enumerate(list_int)]
                
        else:
            print(end="")
            break
    if differ < 1000:
        for i in range(4-len(list_int)):
            list_int.append('0')
            list_int.sort()
            differ = "".join(list_int)
        
if differ != 0:
    print("6174")
    print(f"{integer} reaches 6174 via Kaprekar's routine in {iterations} iterations")
    











    