# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sutton Elliott
# Section:      504
# Assignment:   Indivdual Lab 12b
# Date:         28 November 2022

import numpy as np
import matplotlib as plot
import matplotlib.pyplot as plt

weather= open('WeatherDataCLL.csv', 'r')

#needed lists to get each data item 
maxtemp= []
wind= []
rain=[]
avgtemp= []
mintemp=[]
counter= 0
counter1=[]
months= [1,2,3,4,5,6,7,8,9,10,11,12]
#need both of these to read over the first line with the column headers
row_num= weather.readline()
row_num= weather.readline()

#gets all the data points into a list for each item
while row_num != "":
    line= row_num.split(',')
    maxtemp.append(float(line[4]))
    wind.append(float(line[1]))
    mintemp.append(float(line[5]))
    avgtemp.append(float(line[3]))
    counter+=1
    counter1.append(float(counter))
    row_num = weather.readline()
    
#plot 1- maxtemp and wind speed
plt.plot(counter1, maxtemp, color='r', label='Max Temp')
plt.xlabel('Date')
plt.ylabel('Maximum Temperature, F')
plt.title('Maximum Temperature and Average Wind Speed')
plt.legend(loc='upper right')
plt.twinx()
plt.plot(counter1, wind, color='b', label='Avg Wind')
plt.ylabel('Average Wind Speed, mph')
plt.legend(loc='lower left')
plt.show()

#plot 2- wind speed histogram
plt.hist(wind,bins=30, facecolor='g',rwidth=1.0,edgecolor='k')
plt.title('Histogram of Average Wind Speed')
plt.xlabel('Average Wind Speed, mph')
plt.ylabel('Number of Days')
plt.axis([0.0,20.0,0.0,110.0])
plt.show()

#plot 3- average wind speed v. minimum temp
plt.scatter(mintemp, wind, color='k')
plt.title('Average Wind Speed vs Minimum Temperature')
plt.xlabel('Minimum Temperature, F')
plt.ylabel('Average Wind Speed, mph')
plt.show()

weather.close()

weatherlist=[]
with open('WeatherDataCLL.csv','r') as whether:
    for eachline in whether:
        weather = eachline.strip('\n').split()
        weatherlist.append(weather)

weatherlist.remove(weatherlist[0])

goodlist= []
for i in range(len(weatherlist)):
    string= str(weatherlist[i][0])
    goodlist.append(string.strip(',').split(','))
    
#makes a list for each months max, min, and avg temps
JanAvgTemp= []
FebAvgTemp= []
MarAvgTemp= []
AprAvgTemp= []
MayAvgTemp= []
JunAvgTemp= []
JulAvgTemp= []
AugAvgTemp= []
SepAvgTemp= []
OctAvgTemp= []
NovAvgTemp= []
DecAvgTemp= []
JanMaxTemp= []
FebMaxTemp= []
MarMaxTemp= []
AprMaxTemp= []
MayMaxTemp= []
JunMaxTemp= []
JulMaxTemp= []
AugMaxTemp= []
SepMaxTemp= []
OctMaxTemp= []
NovMaxTemp= []
DecMaxTemp= []
JanMinTemp= []
FebMinTemp= []
MarMinTemp= []
AprMinTemp= []
MayMinTemp= []
JunMinTemp= []
JulMinTemp= []
AugMinTemp= []
SepMinTemp= []
OctMinTemp= []
NovMinTemp= []
DecMinTemp= []

val_month=0
if int(val_month) <= 9:
    MonthKey= str(val_month)
    for eachline in range(len(goodlist)):
        if '1' in goodlist[eachline][0][0] and '/' in goodlist[eachline][0][1]:
            JanAvgTemp.append(int(goodlist[eachline][3]))
            JanMaxTemp.append(int(goodlist[eachline][4]))
            JanMinTemp.append(int(goodlist[eachline][5]))
        if '2' in goodlist[eachline][0][0]:
            FebAvgTemp.append(int(goodlist[eachline][3]))
            FebMaxTemp.append(int(goodlist[eachline][4]))
            FebMinTemp.append(int(goodlist[eachline][5]))
        if '3' in goodlist[eachline][0][0]:
            MarAvgTemp.append(int(goodlist[eachline][3]))
            MarMaxTemp.append(int(goodlist[eachline][4]))
            MarMinTemp.append(int(goodlist[eachline][5]))
        if '4' in goodlist[eachline][0][0]:
            AprAvgTemp.append(int(goodlist[eachline][3]))
            AprMaxTemp.append(int(goodlist[eachline][4]))
            AprMinTemp.append(int(goodlist[eachline][5]))
        if '5' in goodlist[eachline][0][0]:
            MayAvgTemp.append(int(goodlist[eachline][3]))
            MayMaxTemp.append(int(goodlist[eachline][4]))
            MayMinTemp.append(int(goodlist[eachline][5]))
        if '6' in goodlist[eachline][0][0]:
            JunAvgTemp.append(int(goodlist[eachline][3]))
            JunMaxTemp.append(int(goodlist[eachline][4]))
            JunMinTemp.append(int(goodlist[eachline][5]))
        if '7' in goodlist[eachline][0][0]:
            JulAvgTemp.append(int(goodlist[eachline][3]))
            JulMaxTemp.append(int(goodlist[eachline][4]))
            JulMinTemp.append(int(goodlist[eachline][5]))
        if '8' in goodlist[eachline][0][0]:
            AugAvgTemp.append(int(goodlist[eachline][3]))
            AugMaxTemp.append(int(goodlist[eachline][4]))
            AugMinTemp.append(int(goodlist[eachline][5]))
        if '9' in goodlist[eachline][0][0]:
            SepAvgTemp.append(int(goodlist[eachline][3]))
            SepMaxTemp.append(int(goodlist[eachline][4]))
            SepMinTemp.append(int(goodlist[eachline][5]))
            
val_month= 11
if int(val_month) >= 10:
    MonthKey= str(val_month)
    for eachline in range(len(goodlist)):
        if '10' in goodlist[eachline][0][0:2]:
            OctAvgTemp.append(int(goodlist[eachline][3]))
            OctMaxTemp.append(int(goodlist[eachline][4]))
            OctMinTemp.append(int(goodlist[eachline][5]))
        if '1' in goodlist[eachline][0][0:2] :
            NovAvgTemp.append(int(goodlist[eachline][3]))
            NovMaxTemp.append(int(goodlist[eachline][4]))
            NovMinTemp.append(int(goodlist[eachline][5]))
        if '1' in goodlist[eachline][0][0:2]:
            DecAvgTemp.append(int(goodlist[eachline][3]))
            DecMaxTemp.append(int(goodlist[eachline][4]))
            DecMinTemp.append(int(goodlist[eachline][5]))
            
#average values
JanAvg= sum(JanAvgTemp)/len(JanAvgTemp)
FebAvg= sum(FebAvgTemp)/len(FebAvgTemp)
MarAvg= sum(MarAvgTemp)/len(MarAvgTemp)
AprAvg= sum(AprAvgTemp)/len(AprAvgTemp)
MayAvg= sum(MayAvgTemp)/len(MayAvgTemp)
JunAvg= sum(JunAvgTemp)/len(JunAvgTemp)
JulAvg= sum(JulAvgTemp)/len(JulAvgTemp)
AugAvg= sum(AugAvgTemp)/len(AugAvgTemp)
SepAvg= sum(SepAvgTemp)/len(SepAvgTemp)
OctAvg= sum(OctAvgTemp)/len(OctAvgTemp)
NovAvg= sum(NovAvgTemp)/len(NovAvgTemp)
DecAvg= sum(DecAvgTemp)/len(DecAvgTemp)

#minimum temperature
JanMin= min(JanMinTemp)
FebMin= min(FebMinTemp)
MarMin= min(MarMinTemp)
AprMin= min(AprMinTemp)
MayMin= min(MayMinTemp)
JunMin= min(JunMinTemp)
JulMin= min(JulMinTemp)
AugMin= min(AugMinTemp)    
SepMin= min(SepMinTemp)  
OctMin= min(OctMinTemp)
NovMin= min(NovMinTemp)
DecMin= min(DecMinTemp)
            
#maximum temperatures
JanMax= max(JanMaxTemp)
FebMax= max(FebMaxTemp)
MarMax= max(MarMaxTemp)
AprMax= max(AprMaxTemp)
MayMax= max(MayMaxTemp)
JunMax= max(JunMaxTemp)
JulMax= max(JulMaxTemp)
AugMax= max(AugMaxTemp)    
SepMax= max(SepMaxTemp)  
OctMax= max(OctMaxTemp)
NovMax= max(NovMaxTemp)
DecMax= max(DecMaxTemp)

averages= [JanAvg, FebAvg, MarAvg, AprAvg, MayAvg, JunAvg, JulAvg, AugAvg, SepAvg, OctAvg, NovAvg, DecAvg]
minimums= [JanMin, FebMin, MarMin, AprMin, MayMin, JunMin, JulMin, AugMin, SepMin, OctMin, NovMin, DecMin]
maximums= [JanMax, FebMax, MarMax, AprMax, MayMax, JunMax, JulMax, AugMax, SepMax, OctMax, NovMax, DecMax]

#plot 4- max, min, avg temperatures
plt.bar(months,averages, color='y')
plt.plot(months,maximums, color='r',label='High T')
plt.plot(months,minimums, color='b',label='Low T')
plt.legend()
plt.xlabel('Month')
plt.ylabel('Average Temperature, F')
plt.title('Temperature by Month')
plt.show 

whether.close()