# -*- coding: UTF-8 -*-
#Original code from:
#http://ankitvad.github.io/blog/visualizingwhatsappchathistory.html
##
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

# Define inputs
whatsappfile="WhatsApp Chat with Misha Imtiaz.txt" #Whatsapp text file as made by whatsapp.
names=['Siddharth','Misha Imtiaz‬'] #Exactly as it is in the Whatsapp file

#Note that the input text file might have to be manually cleansed depending on what is there.
##
#dates.py


##loading data and splitting dates

for name in names:
    x = open(whatsappfile,"r")
    me = name+":"
    print(me)
    my_date = open(name+"_date"+".txt","w")
    y = x.readline().decode('utf-8-sig').encode('utf-8')
    while y:
            if (me in y):
                temp = y.split(" ",1)
                my_date.write(temp[0]+"\n")	
            y = x.readline().decode('utf-8-sig').encode('utf-8')
    my_date.close();
    del(y)
    print('Data loaded and split');
##
x.close()    
#Cleaning data
#cal_msg.py :
import re
b = open(whatsappfile,"r")
a = open("Messages_"+whatsappfile+".txt","w")
c = open("Exceptions_"+whatsappfile+".txt","w")
y = b.readline().decode('utf-8-sig').encode('utf-8')

while y:
    if(y != '\r\n'):
            temp = y.split(": ",2)            
            try:
                x = temp[1] #SIDS              
                x = re.sub('([\:\;][\)\|\\\/dDOoPp\(\'\"][\(\)DOo]?)','',x)
                x = re.sub('[?\.#_]','',x)
                x = re.sub('[\s]+',' ',x)
                a.write(x+"\n")
            except:
                a.write(" "+"\n")
                c.write(temp[0]+'\n')
          
    y = b.readline()
a.close();
c.close();
print("Lines causing exception in input file written to: " + "Exceptions_"+whatsappfile+".txt")
print('Data cleansed and raw messages saved to '+"messages_"+whatsappfile+".txt")

#
x = open(whatsappfile,"r")

for name in names:
   
    #count dates and Export dates to csv
    x = open(name+"_date"+".txt",'r')
    y = x.read()

    from collections import Counter
    counted= Counter(y.split('\n'))
    outfileme="counted_"+name+".csv"
    with open(outfileme,'w') as f:
        for k,v in  counted.most_common():
            f.write( "{} {}\n".format(k,v) )
    f.close()
    #

