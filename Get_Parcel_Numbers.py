#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:39:22 2020

@author: HJK216
"""

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')

DRIVER_PATH = 'Path To Driver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://recorder.cuyahogacounty.us/searchs/parcelsearchs.aspx')

driver.find_element_by_id('txtRecStart').clear()
driver.find_element_by_id('txtRecStart').send_keys('1/1/1900')

driver.find_element_by_id('txtRecEnd').clear()
driver.find_element_by_id('txtRecEnd').send_keys('12/8/2020')

startnum = 90100000
endnum = 90199999
howmanytimes = endnum - startnum

with open('isparcelvalid.txt', 'w') as f:
    for i in range(howmanytimes):
        list1 = []
        currentnum = startnum + i
        
        driver.find_element_by_id('ParcelID').clear()
        
        PARCEL = str(currentnum)
        
        parcelid = driver.find_element_by_id('ParcelID').send_keys(PARCEL)
        
        beginsearch = driver.find_element_by_id('ValidateButton').click()
        
        try:
            ifin2 = driver.find_element_by_id('ctl00_ContentPlaceHolder1_GridView1')
            driver.execute_script('window.history.go(-1)')
            list1.append(PARCEL)
            list1.append('VALID')
            line = ",".join(list1)
            f.write("%s\n" % line)
            print(PARCEL, ", VALID")
        except:
            list1.append(PARCEL)
            list1.append('INVALID')
            line = ",".join(list1)
            f.write("%s\n" % line)
            print(PARCEL, ", INVALID")
            driver.execute_script("window.history.go(-1)")

driver.quit()
