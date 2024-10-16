myfile= open('mod12activity.txt', 'r')

array= ''
mystr= myfile.readline()

while mystr != '':
    array+= mystr.strip()
    mystr= myfile.readline()
    
print(array)
    
#  B I N G O
#1 t e x a s 
#2 h b r p l
#3 y k i q z
#4 v o c w d
#5 g f m u n

# h  i  d  d  e  n  h  o  w  d  y  a  g  s
#B2 N3 O4 O4 I1 O5 B2 I4 G4 O4 B3 G1 B5 O1
#hiddenhowdyags

# e  n  g  i  n  e  e  r  i  n  g  i  s  f  u  n
#I1 O5 B5 N3 O5 I1 I1 N2 N3 O5 B5 N3 O1 I5 G5 O5
#engineeringisfun

    
