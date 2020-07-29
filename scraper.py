#!/usr/bin/python

# Will take a list of autotrader ad page IDs and scrape useful data from them,
# outputting in .csv format. The scraper function itself can be found in ff1.py

# Takes three arugments, in order:
# 1. an input file name (one line per ad url)
# 2. an output file name (appends by default)


import sys
import csv
import os

import ff1
print ("This is the name of the output target: ", sys.argv[2])

with open(str(sys.argv[1]), 'r') as i_file: # url file
    url_list = i_file.readlines()

if os.path.isfile(sys.argv[2]):
    mode = 'a' #if there is such a file, append it (write from the end)
else:
    mode = 'w' #if there isn't such a file, create it (write from the start)

with open(str(sys.argv[2]), mode, encoding = 'gb18030', newline='') as o_file:
    i = 0
    field_names = [
        'url', 'make', 'model', 'trim', 'manufactured_year',
        'condition', 'transmission', 'body_type', 'doors',
        'engine_size', 'seats', 'fuel_type', 'description', 'price',
        'townAndDistance', 'isTradeSeller', 'emailAddress', 'tax',
        'co2Emissions', 'mileage'
    ]
    print('writing the titles...')
    cwriter = csv.DictWriter(o_file, fieldnames=field_names)

    if mode == 'w':
        print('we are in w mode')
        cwriter.writeheader()
    for u in url_list:
        tmp = ff1.scraper(u)
        print(sys.getdefaultencoding())
        #print('This will be written to the csv file:',tmp)
        cwriter.writerow(tmp)
        i+=1
        if i % 10 == 0:
            print(i)

print('done')
