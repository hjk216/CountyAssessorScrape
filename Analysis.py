#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18

@author: HJK216
"""

from ast import literal_eval

#Copy data from file to propdata array
propdata = []
with open('propertydatacleaned.txt', 'r') as f:
    for line in f:
        temparray = []
        line = literal_eval(line)
        propdata.append(line)

#Average Assessed Market Residential Value
count = 0
averagevalue = 0
for item in propdata:
    if(item[0][len(item[0])-1] == 'R'):
        if(item[2][0][0] == '2020'):
            item[2][0][1] = item[2][0][1].replace(',','')
            if(item[2][0][1] != ''):
                averagevalue = averagevalue + int(item[2][0][1])
                count = count + 1

averagevalue = int(averagevalue / count)
print('Average Assessed Market Home Value: ', averagevalue)
print('Out of', count, 'properties for 2020.')


#How many homes were sold in 2020
salescount = 0
for item in propdata:
    if(item[0][len(item[0])-1] == 'R'):
        try:
            if(item[1][0][0] == '2020'):
                salescount = salescount + 1
        except:
            continue

print()
print('There were,', salescount, 'homes sold in 2020, in Orange, Ohio.')



appreciationdata = []
#Find average, annual appreciation rate, in most recent six year period
averageappreciationrate = 0
appreciationvalues = []

for item in propdata:
    temparray = []
    tempvaluearray = []
    try:
        lastvalue = int(item[2][0][1].replace(',',''))
        sixyearvalue = int(item[2][5][1].replace(',',''))
        tempvalue = (((lastvalue/sixyearvalue)**(1.0/6)) - 1)
        temparray.append(item[0])
        tempvaluearray.append(round(tempvalue, 4))
        temparray.append(tempvaluearray)
        appreciationvalues.append(temparray)
        #Appreciation Data Array
        tempaa = []
        tempaa.append(item[0])
        tempaa.append([tempvalue])
        appreciationdata.append(tempaa)
    except:
        continue

totalappreciation = 0.0
for item in appreciationvalues:
    totalappreciation = totalappreciation + float(item[1][0])
totalappreciation = totalappreciation / len(appreciationvalues)
print('Annual Appreciation in Orange, Ohio: ', str(round(totalappreciation * 100, 2)) + '%')



#Write appreciation data to file
with open('appreciationdata.txt', 'w') as f:
    for item in appreciationdata:
        f.write(str(item))
        f.write('\n')
f.close()
