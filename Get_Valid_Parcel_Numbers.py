#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:41:25 2020

@author: HJK216
"""

#Reads valid parcel numbers from text file and pastes them in new text file
count = 0
with open('isparcelvalid.txt', 'r') as f:
    with open('validparcels.txt', 'w') as f2:
        for line in f:
            line = line.strip('\n')
            linesplit = line.split(',')
            if linesplit[1] == 'VALID':
                f2.write(linesplit[0])
                f2.write('\n')
                count = count + 1

#print("There are", count, "valid parcel numbers in Orange, Ohio.")