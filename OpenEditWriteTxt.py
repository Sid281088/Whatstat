# -*- coding: utf-8 -*-
#This code open a text file. Reads the lines and close text file. Then opens another new text file
#then writes lines to new text file based on an if else stement (see below)

filename='\\asml.com\eu\shared\nl011150\WWW\nonconf\Source_program\09_Laser_beam_delivery_and_control\16-Users\SIDS\m4448\BFSR\xls\02_19_2018_00.00.00.533_SensorLog';
typeoffilein=".xls";
typeoffileout=".xlsx";
infile=filename+typeoffilein;
f = open(infile,"r")
print("opening..."+infile)
#Next, get all your lines from the file:

lines = f.readlines()

#Now you can close the file:

f.close()

#And reopen it in write mode:

f = open(filename+"_edited"+typeoffileout,"w")

#Then, write your lines back, except the line you want to delete. You might want to
#change the "\n" to whatever line ending your file uses.
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

for line in lines:
      #if "+1 (902) 225-0837‬" in line:
       #    pass
       if hasNumbers(line):
        f.write(line)

#At the end, close the file again.
print("writing edited file to..."+filename+"_edited"+typeoffile);
f.close()
