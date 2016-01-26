class seed:
        lowest_temp =0
        highest_temp =0
        buying_price = 0
        name =""
        ideal_altitude = 0

        def __init__(self,name):
                self.name = name
                if(self.name == "Wheat"):
                        self.buying_price = 18
                        self.lowest_temp = 21
                        self.highest_temp = 24
                        self.ideal_altitude = 2000
                elif(self.name == "Rice"):
                        self.buying_price = 85
                        self.lowest_temp = 16
                        self.highest_temp = 27
                        self.ideal_altitude = 2000
                elif(self.name == "Cotton"):
                        self.buying_price = 21
                        self.lowest_temp = 21
                        self.highest_temp = 30
                        self.ideal_altitude = 2600
                elif(self.name == "Jute"):
                        self.buying_price = 20
                        self.lowest_temp = 24
                        self.highest_temp = 35
                        self.ideal_altitude = 1500
                elif(self.name == "Banana"):
                        self.buying_price = 100
                        self.lowest_temp = 27
                        self.highest_temp = 30
                        self.ideal_altitude = 1200
                elif(self.name == "Apple"):
                        self.buying_price = 150
                        self.lowest_temp = 21
                        self.highest_temp = 24
                        self.ideal_altitude = 2100
                else:
                        self.name = "NULL"

        def check_if_right_temp(self,temp):
                if((temp<=self.highest_temp)and(temp>=self.lowest_temp)):
                        return True
                else:
                        return False

                        #decide the boundaries after initialization
        def absolute_difference_between_altitudes(self,altitude):
                difference = altitude - self.ideal_altitude
                if (difference<0):
                        return -1*difference
                else:
                        return difference
