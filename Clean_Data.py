from ast import literal_eval

#Clean data and paste data to new file
with open('propertydata.txt','r') as f:
    with open('propertydatacleaned.txt', 'w') as f2:
        for line in f:
            line = literal_eval(line)
            try:
                if(line[0][1] == 'LW' or line[0][1] == 'R'):
                    if('LISTED WITH' in line[0][0] or 'LISTED WITH' in line[0][1] or 'LISTED WITH' in line[0][0][1]):
                        continue
                    if('LAKES OF ORANGE' in line[0][0][1]):
                        continue
                    if('PINE IX' in line[0][0][1]):
                        continue
                    if('CLEVELAND CITY OF' in line[0][0][1]):
                        continue
                    line[0][0].remove('Field Definitions')
                    line[0][0].pop(1)
                    temparrayone = []
                    temparrayone.append(line[0][0][0])
                    tempzero = ''
                    for i in range(len(line[0][0])):
                        if(i == 1):
                            tempzero = line[0][0][i]
                        if(i > 1):
                            tempzero = tempzero + ', ' + line[0][0][i]
                    temparrayone.append(tempzero)
                    line[0][0] = temparrayone
                    temparray = []
                    tempval = line[0][0]
                    tempval.append(line[0][1])
                    temparray.append(tempval)
                    temparray.append(line[1])
                    temparray.append(line[2])
                    temparray.append(line[3])
                    if(temparray[0][len(temparray[0])-1] != 'LW'):
                        f2.write(str(temparray))
                        f2.write('\n')
            except:
                if(line[0][len(line[0])-1] != 'LW'):
                    f2.write(str(line))
                    f2.write('\n')
                continue
            if(line[0][len(line[0])-1] != 'LW'):
                f2.write(str(line))
                f2.write('\n')
