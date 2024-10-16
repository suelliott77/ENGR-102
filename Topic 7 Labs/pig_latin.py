# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
# Section:      504
# Assignment:   Indivdual lab 7a
# Date:         12 October 2022

#input of words from the user 
sentence= input("Enter word(s) to convert to Pig Latin: \n")

#split the words to different elements of a list 
words= sentence.split()

#for loop to see where vowel is 
for i, word in enumerate(words):
     if word[0] in 'aeiouy':
         words[i] = words[i] + "yay"
         
     else:
         has_vowel = False 
         for j, letter in enumerate(word):
             if letter in 'aeiouy':
                 words[i] = word[j:] + word[:j] + "ay"
                 has_vowel = True
                 break 
         if(has_vowel == False):
             words[i] = words[i]+ "ay"
     
             
pig_latin= ' '.join(words)
print(f'In Pig Latin, "{sentence}" is:',pig_latin)   
        
        


