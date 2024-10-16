# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
# Section:      504
# Assignment:   Indivdual lab 10a
# Date:         16 November 2022

#gets the file to go through with the input statement 
valid = open('valid_barcodes.txt', 'w')
barcodes = input('Enter the name of the file: ')

#gets all the lines to be read into a list 
with open(barcodes, 'r') as myfile:
    counter = 0
    #Separates them into 2 seperate lists that are group 1 and group 2 
    for line in myfile:
        myfile = line
        line = list(line)
        odd_list = []
        even_list = []
        i = 0 
        #gets the list for the odd indexes 
        while i < int(len(line)-3):
            odd_list.append(int(line[i]))
            i += 2
        i = 1
        #gets the list for the even indexes 
        while i < int(len(line)-2):
            even_list.append(int(line[i]))
            i += 2 
            
        #calculations for the sum of the groups 
        sumodd= sum(odd_list)
        sumeven= sum(even_list)
        
        #calculations for multiplication of second and first group
        second = sumeven * 3
        third = second + sumodd
        digit = third % 10 
        number= 10- digit 
        
        #checks if barcode is valid 
        if str(number) == line[-2]:
            counter +=1
            valid.write(f'{myfile}')
        else:
            continue

print(f'There are {counter} valid barcodes')
valid.close()      
        
        



            

            