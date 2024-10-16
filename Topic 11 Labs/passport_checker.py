# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
#               Justin Smonko
#               Vedanti Naktode
#               Jonathon Fulton 
# Section:      504
# Assignment:   Team Lab 11a
# Date:         21 November 2022

#gets the file through the imports and other things
valid = open('valid_passports.txt', 'w')
passports = input('Enter the name of the file: ')

#opens the file and reads life by line 
with open(passports, 'r') as myfile:
    counter= 0
    line= myfile.read().split('\n\n')
    #loops through each of the sets of data and puts into a list to check through if statement
    for i in line:
        if ('byr' in i):
            if ('pid' in i):
                if ('iyr' in i):
                    if ('eyr' in i):
                        if ('hgt' in i):
                            if ('ecl' in i):
                                if('cid' in i):
                                    #adds to the counter 
                                    counter+=1
                                    #if the passport if valid writes it to the file 
                                    valid.write(f'{i}\n\n')
                                    
    
print(f'There are {counter} valid passports')                  
valid.close()
        