# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jonathon Foltyn
#               Justin Smonko
#               Vedanti Naktode
#               sutton Elliot
# Section:      504
# Assignment:   Team Lab 7a
# Date:         10/12/2022

#needed time input from the user
time = input("Enter the time: ")

#numbers in numbers 
#number 0
zero = [
    "000",
    "0 0",
    "0 0",
    "0 0",
    "000"
]
# number 1
one = [
" 1 ",
"11 ",
" 1 ",
" 1 ",
"111"
]
# number 2 
two = [
    "222",
    "  2",
    "222",
    "2  ",
    "222"
]
# number 3
three = [
    "333",
    "  3",
    "333",
    "  3",
    "333"
]
# number 4
four = [
    "4 4",
    "4 4",
    "444",
    "  4",
    "  4"
]
# number 5
five = [
    "555",
    "5  ",
    "555",
    "  5",
    "555"
]
# number 6
six = [
    "666",
    "6  ",
    "666",
    "6 6",
    "666"
]
# number 7
seven = [
    "777",
    "  7",
    "  7",
    "  7",
    "  7"
]
# number 8
eight = [
    "888",
    "8 8",
    "888",
    "8 8",
    "888"
]
#number 9
nine = [
    "999",
    "9 9",
    "999",
    "  9",
    "999"
]
# colons 
colon = [
    " ",
    ":",
    " ",
    ":",
    " "
]

#lists for lines if the time 
line1 = []
line2 = []
line3 = []
line4 = []
line5 = []
# making the numbers from little numbers
display_time = []
def append_to_lines(number):
    line1.append(number[0])
    line2.append(number[1])
    line3.append(number[2])
    line4.append(number[3])
    line5.append(number[4])
time_list = []
for i in time:
    if i == ":":
        line1.append(colon[0])
        line2.append(colon[1])
        line3.append(colon[2])
        line4.append(colon[3])
        line5.append(colon[4])
    else:
        if int(i) == 0:
            append_to_lines(zero)
        if int(i) == 1:
            append_to_lines(one)
        if int(i) == 2:
            append_to_lines(two)
        if int(i) == 3:
            append_to_lines(three)
        if int(i) == 4:
            append_to_lines(four)
        if int(i) == 5:
            append_to_lines(five)
        if int(i) == 6:
            append_to_lines(six)
        if int(i) == 7:
            append_to_lines(seven)
        if int(i) == 8:
            append_to_lines(eight)
        if int(i) == 9:
            append_to_lines(nine)
# appending the different lines toegther 
display_time.append(line1)
display_time.append(line2)
display_time.append(line3)
display_time.append(line4)
display_time.append(line5)
#displaying the clock
def display_clock():
    print()
    for i in display_time:
        for j in i:
            print(j, end=" ")
        print()
#final output 
display_clock()
