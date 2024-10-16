# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
# Section:      504
# Assignment:   Indivdual lab 7b
# Date:         12 October 2022

#input from the user 
text= input("Enter some text: \n")
output=""

#dictonary and split up list of text 
mydict= {'a' : '4', 'e' : '3', 'o' : '0', 's' : '5', 't' : '7'}
words= text.split()
letters= []

for i in (words):
    for j in range(len(i)):
        letters.append(i[j])
        
for letter in letters:
    if letter in mydict:
        letter= mydict[letter]
    output+= letter
    
print(f'In leet speak, "{text}" is:', output)
        