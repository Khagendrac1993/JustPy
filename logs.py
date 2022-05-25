# extract IP, mac address from a log file, and printout vendor of particular mac and save it in a csv file.  
# Khagendra 
import urllib.request as urllib2
import json
import codecs
import re 
import csv
macip= []
umacip = []
u =[]
qq =[]
listip= ("10.172.219.117", "10.192.125.251", "10.172.219.26", "10.191.155.13")
with open('dhcpdsmall.log', 'r') as ipn:
    for line in ipn:
        line.rstrip()
        match =  re.search(r"on (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) to (\w+:\w+:\w+:\w+:\w+:\w+) .* via ", line)
        if match:           
            match1 = match.group(1)
            match2 = match.group(2)
            match3 = match.group(1),  match.group(2)
            macip.append(match3)
            if match1 in listip:
                pp = match1, match2
                if pp not in qq:
                    qq.append(pp)    
    for x, v in qq:
        url = "http://macvendors.co/api/"
        mac_address = v
        request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"}) 
        response = urllib2.urlopen( request )
        reader = codecs.getreader("utf-8")
        obj = json.load(reader(response))
        vendor = (obj['result']['company'])
        denn = v, x, vendor 
        if denn not in u:
            u.append(denn)
    with open("maclist.csv", 'w', newline= "") as fout: # write in a new csv file by creating one 
        csvout = csv.writer(fout)
        csvout.writerow(['IP address', 'Mac address', 'Vendor']) # in row there will be server and IP 
        csvout.writerows(u)
