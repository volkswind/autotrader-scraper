# Listmaker
# Usage:
# ./listmaker.py https://www.autotrader.co.uk/car-search?advert... url_list.txt
# if file exists, we append

# To use it in cmd, here is one example:
# remember to include "" for both the link and the file name
# python listmaker.py "https://www.autotrader.co.uk/car-search?advertising-location
# =at_cars&postcode=cv325xe&guid=20c6ac3f
# -9cc1-4378-a2b2-fa1fbed898b2&model=ELISE" "url_list.txt"
import sys
import csv
import os

import ff1
print ("This is the input url ", sys.argv[1])
print ("This is the output text file ", sys.argv[2])
base_url = sys.argv[1]
out_fname = sys.argv[2]

if not os.path.isfile(out_fname):
    z = open(out_fname, 'w')
    z.close()

page_count = 1
while True:
    results = ff1.search_result_scraper(base_url + '&page=' + str(page_count))
    if len(results) > 0:
        with open(out_fname, 'a') as fcon:
            for r in results:
                fcon.write('https://www.autotrader.co.uk' + r)
                fcon.write('\n')
        page_count += 1
        print(page_count)
        print(len(results))
    else:
        break
