# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
# Section:      504
# Assignment:   Indivdual lab 10c
# Date:         16 November 2022

weather= open('WeatherDataCLL.csv', 'r')

max_temp= []
min_temp= []
rain= []
counter= 0 
#need both of these to read over the first line with the column headers
row_num= weather.readline()
row_num= weather.readline()

#goes line by line and takes certain parts of each for list 
while row_num != "":
    line= row_num.split(',')
    max_temp.append(int(line[4]))
    min_temp.append(int(line[5]))
    rain.append(float(line[2]))
    counter+=1
    row_num = weather.readline()

#takes the lists made above and gets wanted values 
max_temp= max(max_temp)
min_temp= min(min_temp)
average_rain = sum(rain) / counter
print(f'3-year maximum temperature: {max_temp} F')
print(f'3-year minimum temperature: {min_temp} F')
print(f'3-year average precipitation: {average_rain:.3f} inches')
print()

weather.close()


days=0
rainydays= 0
avgtemp= []
avgwind= []

weather= open('WeatherDataCLL.csv', 'r')

month= input('Please enter a month: \n')
year= input('Please enter a year: \n')

mydict= {'January':'1', 'February':'2','March':'3','April':'4',
         'May':'5', 'June':'6','July':'7','August':'8','September':'9',
         'October':'10','November':'11','December':'12'}
month_num = mydict[month]
#need both of these to read over the first line with the column headers
line= weather.readline()
line= weather.readline()
while line != '':
    line = line.split(',')
    #only goes through the other if statements if the years are the same
    if line[0][-4:] == year:
        #goes through the single digit days of the correct year and month
        if line[0][:-7] == month_num and line[0][-7] == '/':
            #adds numbers to each of the lists
            avgtemp.append(float(line[4]))
            avgwind.append(float(line[1]))
            days+=1
            #adds to rainydays if the amount of rain isn't 0
            if float(line[2]) != 0:
                rainydays += 1
        #goes through double digit days of the correct year and month
        if line[0][:-8] == month_num and line[0][-8] == '/':
            avgtemp.append(float(line[4]))
            avgwind.append(float(line[1]))
            days+=1
            if float(line[2]) != 0:
                rainydays += 1
    line = weather.readline()
    
#needed values given the lists that we created above     
avgtemp= sum(avgtemp)/len(avgtemp)
avgwind= sum(avgwind)/len(avgwind)
precip= (rainydays / days) * 100
print(f'For {month} {year}:')
print(f'Mean maximum daily temperature: {avgtemp:.1f} F')
print(f'Mean daily wind speed: {avgwind:.2f} mph')
print(f'Percentage of days with precipitation: {precip:.1f}%')
weather.close()
    
