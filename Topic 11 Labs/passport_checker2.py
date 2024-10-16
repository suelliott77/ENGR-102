# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
#               Justin Smonko
#               Vedanti Naktode
#               Jonathon Fulton 
# Section:      504
# Assignment:   Team Lab 11b
# Date:         21 November 2022

file = input("Enter the name of the file: ")

checker = open(file, "r")

adding = open("valid_passports2.txt", "w")
#splits each individual passport into an element in a list
long = checker.read().split("\n\n")

counter = 0
valid = 0
p = False
eyecolor = ["amb", "blu", "brn", "gry", "grn", "hzl","oth"]

for i in long:
    if ("byr" in i) and ("iyr" in i) and ("eyr" in i) and ("hgt" in i) and ("ecl" in i) and ("pid" in i) and ("cid" in i):
        #split each field into an element in a string
        checking = i.split("\n")
        checking1 = " ".join(checking)
        final = checking1.split(" ")
        #sort alphabetically
        sfinal = sorted(final)

        
        # --- byr
        byr = int(sfinal[0][-4:])
        if byr >= 1920 and byr <= 2005:
            valid += 1
        if byr == 1931:
            p = True
        
        # --- cid 
        cid = sfinal[1][-3:]
        if len(sfinal[1]) == 7 and cid[0] != "0":
            valid += 1
        
        # --- ecl
        ecl = sfinal[2][-3:]
        if ecl in eyecolor:
            valid += 1
            
        # --- eyr
        eyr = int(sfinal[3][-4:])
        
        if eyr >= 2022 and eyr <= 2032:
            valid += 1
        
        # --- hgt
        if len(final) == 8: #hcl
            extra = 1
        else:
            extra = 0
            #check if cm or in
        hgt = sfinal[4 + extra]
        if hgt[-2:] == "cm":
            if len(hgt) == 9:
                if int(hgt[4:7]) >= 150 and int(hgt[4:7]) <= 193:
                    valid += 1
        if hgt[-2:] == "in":
            if len(hgt) == 8:
                if int(hgt[4:6]) >= 59 and int(hgt[4:6]) <= 76:
                    valid += 1
                        
        # --- iyr
        iyr = sfinal[5 + extra]
        if(len(iyr) == 8):
            yr = int(iyr[-4:])
            if yr >= 2012 and yr <= 2022:
                valid += 1
            
        # --- pid
        pid = sfinal[6 + extra]
        if len(pid) == 13:
            valid += 1
       
        
        if valid == 7:
            adding.write(i)
            counter += 1
            adding.write("\n\n")
        
        valid = 0
checker.close()
adding.close()
print(f"There are {counter} valid passports")  