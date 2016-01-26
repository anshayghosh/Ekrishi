import time
import urllib
import re
import webbrowser
import contextlib
import os

class crop:
        selling_price = 0
        life = 0
        decrementation_factor =0.05
        current_time = 0
        harvest_life = 50
        harvest_time = 0
        harvest_boundary =25
        life_boundary = 10
        name = ""
        start_time = 0

        def __init__(self,name):
                self.name = name
                if(self.name == "Wheat"):
                        self.selling_price = 220
                        self.harvest_time = 80
                elif(self.name == "Rice"):
                        self.selling_price = 250
                        self.harvest_time = 100
                elif(self.name == "Cotton"):
                        self.selling_price = 445
                        self.harvest_time = 120
                elif(self.name == "Jute"):
                        self.selling_price = 270
                        self.harvest_time = 90
                elif(self.name == "Banana"):
                        self.selling_price = 165
                        self.harvest_time = 560
                elif(self.name == "Apple"):
                        self.selling_price = 470
                        self.harvest_time = 120
                else:
                        self.name = "NULL"
                        self.decrementation_factor = 0
        

        #havent decided how much water increases life
        def water(self):
                if(self.check_dead_status() == False):
                        self.life = self.life+5

        def decrement_life(self):
                if(self.check_dead_status() == False):
                        self.life = self.life-decrementation_factor

        def printLife(self):
                return self.life

        #decide values for boundaries during implementation
        def check_harvest_status(self):
                if((self.current_time <= self.harvest_time+self.harvest_boundary) and (self.current_time >= self.harvest_time-self.harvest_boundary)):
                        if((self.life<=self.harvest_life+self.life_boundary) and (self.life>=self.harvest_life-self.life_boundary)):
                                return True
                return False

        

        def check_dead_status(self):
                if((self.current_time>=self.harvest_time+30)  or (self.life<-5) or (self.life>=self.harvest_life+self.life_boundary)):
                        return True
                else:
                        return False

        def get_selling_price(self):
            const= self.selling_price
            try:
                text=readWebPage("http://agmarknet.nic.in/rep1Newx1_today.asp")
                strbefore=""

                if(self.name=="Wheat"):
                        strbefore="<font color=\"#000080\">Maharashtra 2189</font> </a></font> </td>"
                elif(self.name=="Rice"):
                        strbefore="<font color=\"#000080\">Sona Mansoori Non Basmati</font> </a></font> </td>"
                elif(self.name=="Cotton"):
                        strbefore="<font color=\"#000080\">Cotton (Unginned)</font> </a></font> </td>"
                elif(self.name=="Jute"):
                        strbefore="<font color=\"#000080\">TD-5</font> </a></font> </td>"
                elif(self.name =="Banana"):
                        strbefore="<font color=\"#000080\">Banana - Ripe</font> </a></font> </td>"
                elif(self.name=="Apple"):
                        strbefore="<font color=\"#000080\">Apple</font> </a></font> </td>"

                startOfTemp = text.find(strbefore)
                index = startOfTemp + len(strbefore)
                symbol_counter = 0
                while(True):
                        if(text[index]=='>'):
                            symbol_counter = symbol_counter+1
                        if(symbol_counter==12):
                            break;
                        index=index+1
                index = index+2
                begin_index = index
                ch = text[index]

                while ch != '<':
                        index = index+1
                        ch = text[index]

                self.selling_price=int((int(text[begin_index:index]))/10)
            except:
                self.selling_price=const


def readWebPage(url):
        with contextlib.closing(urllib.urlopen(url)) as fin:
                return fin.read()

x = crop("Wheat")
print(x.selling_price)
x.get_selling_price()
print(x.selling_price)
