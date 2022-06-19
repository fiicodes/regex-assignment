# importing all necessar modules
import os
import sys

import re
from bs4 import BeautifulSoup
import pandas as pd
#path for the html file
path='sample-example.html'
#parsing the html file
list_header=[]
soup= BeautifulSoup(open(path),'html.parser')
header = soup.find_all("table")[0].find("tr")
leaderboard=soup.find('table')
tbody=leaderboard.find('tbody')


#regular expression for referrance number
referrancenoreg="[A-Z]{2}\d{8}-\d{5}"
#regular expression for all data in the table
regx=["[A-Z]{2}\d{8}-\d{5}","\(\d{3}\)\s\d{3}-\d{4}","[A-Za-z]{3,}\s[A-Za-z]{3,}","[A-Za-z]{6}\s[A-Za-z]{5,}","\s\d{5,}","N\/A","\sn\/a","\d{2}\s\w{3}\s\d{4}\s\d{2}:\d{2}\s[A-Z]{2}","[A-Za-z]{6}\s[A-Za-z]{5,}","[A-Z]{9}","\d{4}\s\w{1,}\s\w{1,}(\s\w{2})?\W\s*\w{1,}\s\w{1,}\W\s\w{2}\W\s\d{5}","(\w{1,}\s*\w{1,}\s\w{1,},\s)?(\w{1,}\s)?(\w{1,},\s)?(\w(1,)\s)?(\w{1,}\s)?(\w{1,}\s)?(\w{1,}\s\w{1,},\s)?\w{1,},\s*(\s*|\w{1,})\s\w{1,},\s\w{1,},.\d{5}"]
f = open("mytable.txt", "w")
for tr in tbody.find_all('tr'):

    #fetching referrance number and storing in list
    refno=[td.text for td in  tr.find_all('a',text=re.compile(referrancenoreg))]
     #fetching all table data 
    data1=[ td.text for td in tr.find_all('td',text=re.compile( '|'.join( regx) ))]
    data1.insert(0,refno[0])

    for character in data1:
        f.writelines(character)
        f.writelines('  ')
    f.writelines('\n\n')
    
   

   

   
        

        
     
        






    




  


   
    
    

    
