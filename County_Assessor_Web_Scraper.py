#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:59:31 2020

@author: HJK216
"""

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')

DRIVER_PATH = 'Path To Driver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://myplace.cuyahogacounty.us/')

#Read and store valid parcel numbers from list
validparcellist = []
with open('validparcels55.txt','r') as f:
    for line in f:
        line = line.strip('\n')
        if(len(line) == 8):
            validparcellist.append(line)
        else:
            print("INVALID PARCEL DETECTED")
            exit()
f.close()


#Navigates to county assessor and searches through the valid parcel numbers, saving data to file
with open('propertydata55.txt', 'w') as f:
    for parcel in validparcellist:
        #Search parcel number
        driver.find_element_by_id("txtData").clear()
        driver.find_element_by_id("Parcel").click()
        driver.find_element_by_id("txtData").send_keys(parcel)
        driver.find_element_by_id("btnSearch").click()

        try:
            driver.find_element_by_id("btnGeneralInfo").click()
        except:
            continue

        propertyone = []

        #Get parcel number & address
        address = driver.find_element_by_id("viewPropertyHeader")
        address = str(address.text).split('\n')
        addresslist = []

        if(len(address) == 2):
            addresslist.append(address[0])
        elif(len(address) == 3):
            addresslist.append(address[0])
            addresslist.append(address[1] + ', ' + address[2])
        elif(len(address) == 5):
            addresslist.append(address[0])
            addresslist.append(address[2] + ', ' + address[3])
        else:
            addresslist.append(address)

        ###Get property class
        propertyclassweb = driver.find_elements_by_class_name("dataBody")
        propertyclassweb = propertyclassweb[0].text.split('\n')

        ###Append parcel, address, property class to list
        if(propertyclassweb[8] != 'Tax Abatement'):
            addresslist.append(propertyclassweb[8])
        propertyone.append(addresslist)



        #Get transfers
        driver.find_element_by_id("btnTransferInfo").click()

        ###Get number of transfers
        count = 0
        headeridlist = []
        mybool = True
        while mybool:
            try:
                startingstr = "ui-accordion-accordion-header-"
                currentstr = startingstr + str(count)
                transferid = driver.find_element_by_id(currentstr)
                headeridlist.append(currentstr)
                count = count + 1
            except:
                mybool = False

        ###Get transfer data
        transferlist = []

        c = 0
        s = 0
        for transfer in headeridlist:
            transfercurrent = []
            transferdate = driver.find_element_by_id(transfer)
            transferdate = str(transferdate.text).strip("Transfer Date: ")
            transfercurrent.append(transferdate)

            driver.find_element_by_id(transfer).click()
            transferone = driver.find_elements_by_class_name("text-nowrap")

            c = 0
            for i in transferone:
                if i.text == "Sales Amt" and c > s:
                    transfercurrent.append(transferone[c+7].text)
                c = c + 1
            s = s + 16

            try:
                if(transfercurrent[1] != '$.00' and transfercurrent[1] != ''):
                    transfercurrent[0] = transfercurrent[0][6:10]
                    transfercurrent[1] = transfercurrent[1][1:]
                    if('.00' in transfercurrent[1]):
                        transfercurrent[1] = transfercurrent[1].replace('.00','')
                    transferlist.append(transfercurrent)
                else:
                    continue
            except:
                continue

        propertyone.append(transferlist)

        #Get values
        driver.find_element_by_id('btnValuesInfo').click()
        valuehistory = driver.find_elements_by_class_name("dataBody")
        valuehistory = valuehistory[0].text.split('\n')
        valuehistory.remove('Value History')
        valuehistorylist = []

        for item in valuehistory:
            temparray = []
            temparray.append(item[10:14])
            temparray.append(item[31:len(item)])
            valuehistorylist.append(temparray)

        propertyone.append(valuehistorylist)

        #If no values, do not include
        if(len(valuehistorylist) == 1):
            continue

        #Get permits
        driver.find_element_by_id('btnPropertyCardInfo').click()
        permitsectionlist = []

        tr = 1
        td = 0
        while(True):
            if(td % 7 == 0):
                tr = tr + 1
                td = 0
            td = td + 1
            try:
                permitsectionlist.append(driver.find_element_by_xpath("//table[@class='PropertyCardImprovementsTable']//tr[{}]//td[{}]".format(tr,td)).text)
            except:
                break

        permitslist = []
        permit = []

        tr = tr - 2
        year = 0
        reason = 1
        addtax = 2

        for i in range(tr):
            if(permitsectionlist[addtax] != '$'):
                permit.append(permitsectionlist[year])
                permit.append(permitsectionlist[reason][5:])
                permit.append(permitsectionlist[addtax][1:])
                permitslist.append(permit)

            permit = []
            year = year + 7
            reason = reason + 7
            addtax = addtax + 7

        propertyone.append(permitslist)

        f.write('%s\n' % propertyone)
        
        #To verify program is running
        print(parcel)

driver.close()
print('Program Complete')
