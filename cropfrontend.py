from Tkinter import*
from eventBasedAnimationClass import EventBasedAnimationClass
import random
import copy
from input import*
import seed_optimization_and_message
from sms_tester import*


class FarmGame(EventBasedAnimationClass):
	def __init__(self, number):
		self.width = 1000
		self.height = 750
		self.number=number
		super(FarmGame,self).__init__(self.width,self.height)

	def initAnimation(self):

		#init screens
		canvas=self.canvas
		self.startScreen=True
		self.helpScreen=False
		self.farmScreen=False
		self.marketScreen=False
		self.infoScreen=False
		self.gameOverScreen=False
		self.counter=0
		self.back=PhotoImage(file="piche.gif")
		
		self.cottonScreen=False
		self.riceScreen=False
		self.wheatScreen=False
		self.appleScreen=False
		self.juteScreen=False
		self.bananaScreen=False
		
		self.counter=0
		self.currRow=None
		self.currCol=None

		self.timeDecrease=1
		self.timeLeft=10

		self.altitude=None
		self.temp=None
		self.latlng=None
		self.address=None
		self.expCrop=None

		self.startScreenImage= PhotoImage(file="EKrishi.gif")
		self.farmScreenImage= PhotoImage(file="farm.gif")
		self.marketScreenImage=PhotoImage(file="SHOPMAIN.gif")
		self.gameOverScreenImage= PhotoImage(file="GameOver.gif")
		self.infoScreenImage= PhotoImage(file="NIRDESH.gif")
		self.janky=PhotoImage(file="JANKY.gif")

		self.sms2=PhotoImage(file="orangeisthe.gif")
		self.sms=PhotoImage(file="newblack.gif")
		self.ish= PhotoImage(file="ish.gif")


		self.rice= PhotoImage(file="RICE.gif")
		self.wheat= PhotoImage(file="WHEAT.gif")
		self.banana= PhotoImage(file="Banana.gif")
		self.apple= PhotoImage(file="APPLES.gif")
		self.cotton=PhotoImage(file="COTTON.gif")
		self.jute= PhotoImage(file="JUTE.gif")
		self.soil=PhotoImage(file="soil.gif")
		self.soil2=PhotoImage(file="soil2.gif")

		#farm cells
		self.appleBox=PhotoImage(file="appleBox.gif")
		self.appleBox2=PhotoImage(file="appleBox2.gif")
		self.bananaBox=PhotoImage(file="bananaBox.gif")
		self.bananaBox2=PhotoImage(file="bananaBox2.gif")
		self.wheatBox=PhotoImage(file="wheatBox.gif")
		self.wheatBox2=PhotoImage(file="wheatBox2.gif")
		self.riceBox=PhotoImage(file="riceBox.gif")
		self.riceBox2=PhotoImage(file="riceBox2.gif")
		self.juteBox=PhotoImage(file="juteBox.gif")
		self.juteBox2=PhotoImage(file="juteBox2.gif")
		self.cottonBox=PhotoImage(file="cottonBox.gif")
		self.cottonBox2=PhotoImage(file="cottonBox2.gif")

		#mktplace boxes
		self.newWheat=PhotoImage(file="newWheat.gif")
		self.newRice=PhotoImage(file="newRice.gif")
		self.newBanana=PhotoImage(file="newBanana.gif")
		self.newApple=PhotoImage(file="newApple.gif")
		self.newCotton=PhotoImage(file="newCotton.gif")
		self.newJute=PhotoImage(file="newJute.gif")

		#janky 
		self.fapple=PhotoImage(file="fapple.gif")
		self.frice=PhotoImage(file="frice.gif")
		self.fbanana=PhotoImage(file="fbanana.gif")
		self.fjute=PhotoImage(file="fjute.gif")
		self.fcotton=PhotoImage(file="fcotton.gif")
		self.fwheat=PhotoImage(file="fwheat.gif")

		#flashcards
		self.riceFlash=PhotoImage(file="riceFlash.gif")
		self.wheatFlash=PhotoImage(file="wheatFlash.gif")
		self.cottonFlash=PhotoImage(file="cottonFlash.gif")
		self.juteFlash=PhotoImage(file="juteFlash.gif")
		self.appleFlash=PhotoImage(file="appleFlash.gif")
		self.bananaFlash=PhotoImage(file="bananaFlash.gif")

		self.danger=PhotoImage(file="danger.gif")

		self.plus=PhotoImage(file="plus.gif")

		self.normalDict= {'NULL':self.soil,'Rice':self.riceBox,'Wheat':self.wheatBox,'Cotton':self.cottonBox,'Jute':self.juteBox,'Banana':self.bananaBox,'Apple': self.appleBox}
		self.highlightDict= {'NULL':self.soil2,'Rice':self.riceBox2,'Wheat':self.wheatBox2,'Cotton':self.cottonBox2,'Jute':self.juteBox2,'Banana':self.bananaBox2,'Apple': self.appleBox2}

		self.selected=None

		self.root.bind("<Motion>", lambda event: self.onMouseMotion(event))

		self.crop_matrix = [[crop("NULL") for x in range(5)] for x in range(5)]
		self.seed_list = []
		self.bank = bank(250)
		self.numSeeds = [0,0,0,0,0,0]
		self.seed_list.append(seed("Rice"))
		self.seed_list.append(seed("Wheat"))
		self.seed_list.append(seed("Cotton"))
		self.seed_list.append(seed("Jute"))
		self.seed_list.append(seed("Banana"))
		self.seed_list.append(seed("Apple"))
		self.flashDict={"Wheat": self.fwheat, "Rice": self.frice, "Cotton": self.fcotton, "Jute": self.fjute, "Banana": self.fbanana, "Apple": self.fapple}
		self.getEverything()

		self.rice1=crop("Rice")
		self.rice1.get_selling_price()
		self.wheat1=crop("Wheat")
		self.wheat1.get_selling_price()
		self.cotton1=crop("Cotton")
		self.cotton1.get_selling_price()
		self.jute1=crop("Jute")
		self.jute1.get_selling_price()
		self.banana1=crop("Banana")
		self.banana1.get_selling_price()
		self.apple1=crop("Apple")
		self.apple1.get_selling_price()


	def send_message_of_best_seed(self,seedname, number):
	    sms ='After reading up, I think the best seed to buy right now is '+seedname
	    r = send_message('gmai513', 'a046ac48f5f8e72037f81ebe5f5ea41572375dd1',
	        sms_from='9920241690',  # sms_from='8808891988',
	        sms_to=number, # sms_to='9052161119',
	        sms_body=sms)
	    print r.status_code
	    pprint(r.json())

	def getEverything(self):
		try:
			self.temp=get_temperature()
		except:
			self.temp=24.3
		try:
			self.altitude=get_altitude()
		except:
			self.altitude=7.366
		try:
			self.address=get_address()
		except:
			self.address="Mumbai, Maharashtra"
		try:
			self.expCrop=find_most_optimized_crop(self.seed_list, self.temp, self.altitude)
		except:
			self.expCrop="Jute"

	def onMousePressed(self, event):
		(self.x, self.y)=(event.x, event.y)
		if self.startScreen==True:
			self.startScreen=False
			self.helpScreen=True
		
		elif self.helpScreen==True:
			self.helpScreen=False
			self.farmScreen=True
		
		elif self.farmScreen==True:
			
			#mandi
			if (30<=self.x<=428 and 577<=self.y<=640):
				self.farmScreen=False
				self.marketScreen=True

			#jank
			elif (30<=self.x<=428 and 661<=self.y<=724):
				self.farmScreen=False
				self.infoScreen=True

			#s1
			if (467<=self.x<=532 and 598<=self.y<=663):
				self.selected=0

			# #s2
			elif (550<=self.x<=615 and 598<=self.y<=663):
				self.selected=1


			# #s3
			elif (632<=self.x<=697 and 598<=self.y<=663):
				self.selected=2

			# #s4
			elif (715<=self.x<=780 and 598<=self.y<=663):
				self.selected=3

			# #s5
			elif (798<=self.x<=863 and 598<=self.y<=663):
				self.selected=4

			# #s6
			elif (883<=self.x<=948 and 598<=self.y<=663):
				self.selected=5
			
			else:
				if (30>=self.x or self.x>=970 or self.y<=100 or self.y>=560):
					self.selected=None


			#back
			if (794<=self.x<=970 and 24<=self.y<=87):
				self.farmScreen=False
				self.helpScreen=True

			if (30<=self.x<=970 and 110<=self.y<=560):
				self.plantTree()
		
		elif self.marketScreen==True:
			#back
			if (794<=self.x<=970 and 24<=self.y<=87):
				self.marketScreen=False
				self.farmScreen=True

			#rice
			elif 40<=self.hoverX<=175 and 148<=self.hoverY<=283:
				self.marketScreen=False
				self.riceScreen=True

			#cotton
			elif 40<=self.hoverX<=175 and 348<=self.hoverY<=483:
				self.marketScreen=False
				self.cottonScreen=True


			#banana
			elif 40<=self.hoverX<=175 and 547<=self.hoverY<=682:
				self.marketScreen=False
				self.bananaScreen=True
			#wheat 
			elif 311<=self.hoverX<=446 and 148<=self.hoverY<=283:
				self.marketScreen=False
				self.wheatScreen=True

			#jute
			elif 311<=self.hoverX<=446 and 348<=self.hoverY<=483:
				self.marketScreen=False
				self.juteScreen=True

			#apple
			elif 311<=self.hoverX<=446 and 547<=self.hoverY<=682:
				self.marketScreen=False
				self.appleScreen=True


			#following are for adding seeds:

			#rice
			if 185<=self.hoverX<=247 and 118<=self.hoverY<=207.1:
				if self.bank.bank_balance>=self.seed_list[0].buying_price:
					self.numSeeds[0]+=1
					self.bank.bank_balance-=self.seed_list[0].buying_price

			#wheat
			elif 455<=self.hoverX<=517 and 116<=self.hoverY<=205.1:
				if self.bank.bank_balance>=self.seed_list[1].buying_price:
					self.numSeeds[1]+=1
					self.bank.bank_balance-=self.seed_list[1].buying_price

			#cotton 
			elif 185<=self.hoverX<=247 and 316<=self.hoverY<=405.1:
				if self.bank.bank_balance>=self.seed_list[2].buying_price:
					self.numSeeds[2]+=1
					self.bank.bank_balance-=self.seed_list[2].buying_price

			#jute
			elif 455<=self.hoverX<=517 and 316<=self.hoverY<=405.1:
				if self.bank.bank_balance>=self.seed_list[3].buying_price:
					self.numSeeds[3]+=1
					self.bank.bank_balance-=self.seed_list[3].buying_price

			#banana
			elif 185<=self.hoverX<=247 and 518<=self.hoverY<=607.1:
				if self.bank.bank_balance>=self.seed_list[4].buying_price:
					self.numSeeds[4]+=1
					self.bank.bank_balance-=self.seed_list[4].buying_price

			#apple
			elif 455<=self.hoverX<=517 and 518<=self.hoverY<=607.1:
				if self.bank.bank_balance>=self.seed_list[5].buying_price:
					self.numSeeds[5]+=1
					self.bank.bank_balance-=self.seed_list[5].buying_price

		elif self.riceScreen==True:
			#back
			if (794<=self.x<=970 and 24<=self.y<=87):
				self.riceScreen=False
				self.marketScreen=True

		elif self.wheatScreen==True:
			#back
			if (794<=self.x<=970 and 24<=self.y<=87):
				self.wheatScreen=False
				self.marketScreen=True

		elif self.cottonScreen==True:
			#back
			if (794<=self.x<=970 and 24<=self.y<=87):
				self.cottonScreen=False
				self.marketScreen=True

		elif self.juteScreen==True:
			#back
			if (794<=self.x<=970 and 24<=self.y<=87):
				self.juteScreen=False
				self.marketScreen=True

		elif self.bananaScreen==True:
			#back
			if (794<=self.x<=970 and 24<=self.y<=87):
				self.bananaScreen=False
				self.marketScreen=True

		elif self.appleScreen==True:
			#back
			if (794<=self.x<=970 and 24<=self.y<=87):
				self.appleScreen=False
				self.marketScreen=True

		elif self.gameOverScreen==True:
			if (301<=self.x<=699 and 335<=self.y<=401):
				self.gameOver=False
				self.farmScreen=True
				self.initAnimation()
		elif self.infoScreen==True:
			if (678<=self.x<=864 and 236<=self.y<=303):
				self.infoScreen=False
				self.farmScreen=True
			if 739<=self.hoverX<=841 and 40<=self.hoverY<=93:
				self.send_message_of_best_seed(self.expCrop, self.number)

			

	def onMouseMotion(self, event):
		(self.hoverX,self.hoverY)=(event.x, event.y)
		if self.farmScreen==True:
			#s1
			if (467<=self.hoverX<=532 and 598<=self.hoverY<=663) and self.selected==None:
				self.rice=PhotoImage(file="RICE2.gif")

			else:
				self.rice=PhotoImage(file="RICE.gif")

			# #s2
			if (550<=self.hoverX<=615 and 598<=self.hoverY<=663) and self.selected==None:
				self.wheat= PhotoImage(file="WHEAT2.gif")

			else:
				self.wheat= PhotoImage(file="WHEAT.gif")

			# #s3
			if (632<=self.hoverX<=697 and 598<=self.hoverY<=663) and self.selected==None:
				self.cotton=PhotoImage(file="COTTON2.gif")

			else:
				self.cotton=PhotoImage(file="COTTON.gif")

			# #s4
			if (715<=self.hoverX<=780 and 598<=self.hoverY<=663) and self.selected==None:
				self.jute=PhotoImage(file="JUTE2.gif")

			else:
				self.jute=PhotoImage(file="JUTE.gif")


			# #s5
			if (798<=self.hoverX<=863 and 598<=self.hoverY<=663) and self.selected==None:
				self.banana=PhotoImage(file="BANANA2.gif")

			else:
				self.banana=PhotoImage(file="Banana.gif")

			# #s6
			if (883<=self.hoverX<=948 and 598<=self.hoverY<=663) and self.selected==None:
				self.apple=PhotoImage(file="APPLES2.gif")

			else:
				self.apple=PhotoImage(file="APPLES.gif")

			if (30<=self.hoverX<=970 and 110<=self.hoverY<=560):
				self.currCol= (self.hoverX-30)/189
				self.currRow= (self.hoverY-110)/91
			else:
				(self.currCol, self.currRow)=(None,None)
		
	
	def onKeyPressed(self, event):
		if (event.char=='w'):
			self.waterPlant()
		elif (event.char=='h'):
			self.harvestPlant()

	def drawPercentages(self):
		for row in xrange(5):
			for col in xrange(5):
				if (self.crop_matrix[row][col].name!="NULL"):
					percent= (self.crop_matrix[row][col].current_time)/(self.crop_matrix[row][col].harvest_time)*100
					self.canvas.create_text(28+94+col*189, 106+45+row*91, text=str(int(percent))+"%", font="Helvetica 35 bold" )

	def drawFarmScreen(self):
		for row in xrange(5):
			for col in xrange(5):
				currImg= self.normalDict[self.crop_matrix[row][col].name]
				self.canvas.data["currImg"]=currImg
				currImg=self.canvas.data["currImg"]
				self.canvas.create_image(28+94+col*189, 106+45+row*91, image=currImg)
			

		if self.bank.bank_balance<=20:
			self.timeLeft= self.timeLeft-0.1
		else:
			self.timeLeft=10
		if (self.timeLeft)<10:
			danger= self.danger
			self.canvas.data["danger"]=danger
			danger=self.canvas.data["danger"]
			self.canvas.create_image(710.5, 55.5, image=danger)
			self.canvas.create_text(710.5, 55.5, text="0:0"+str(int(self.timeLeft)), fill="white" ,font="Helvetica 35 bold")

	def waterPlant(self):
		if self.currRow!=None and self.currCol!=None:
			self.crop_matrix[self.currRow][self.currCol].water()


	def harvestPlant(self):
		if self.currRow!=None and self.currCol!=None:
			cell=self.crop_matrix[self.currRow][self.currCol]
			if cell.name!="NULL" and cell.check_harvest_status():
				cell.get_selling_price()
				self.bank.add(cell.selling_price)
				self.crop_matrix[self.currRow][self.currCol]=crop("null")

	def plantTree(self):
		if (self.selected!=None):
			if (self.numSeeds[self.selected]>0):
				if (self.crop_matrix[self.currRow][self.currCol].name=="NULL"):
					self.numSeeds[self.selected]-=1
					newPlant= crop(self.seed_list[self.selected].name)
					self.crop_matrix[self.currRow][self.currCol]=newPlant


	def redrawAll(self):
		canvas=self.canvas
		canvas.delete(ALL)
		self.counter= self.counter+0.1
		#print int(self.counter)
		if self.startScreen==True:
			image= self.startScreenImage
			self.canvas.data["image"]=image
			image = self.canvas.data["image"]
			self.canvas.create_image(self.width/2,self.height/2, image=image)
		
		elif self.helpScreen==True:
			image= self.infoScreenImage
			self.canvas.data["image"]=image
			image = self.canvas.data["image"]
			self.canvas.create_image(self.width/2,self.height/2, image=image)
		
		elif self.farmScreen==True:
			self.removeDead()
			self.incrementTime()
			self.decrementLife()
			image1= self.farmScreenImage
			self.canvas.data["image1"]=image1
			image1=self.canvas.data["image1"]
			self.canvas.create_image(self.width/2, self.height/2, image=image1)
			self.canvas.create_text(562.5, 56, text=str(self.bank.bank_balance), fill="white", font= "Helvetica 35 bold")

			#for the little rectangles at the bottom
			if self.selected==0:
				self.rice=PhotoImage(file="RICE2.gif")
				self.wheat= PhotoImage(file="WHEAT.gif")
				self.cotton=PhotoImage(file="COTTON.gif")
				self.jute=PhotoImage(file="JUTE.gif")
				self.banana=PhotoImage(file="Banana.gif")
				self.apple=PhotoImage(file="APPLES.gif")
			elif self.selected==1:
				self.rice=PhotoImage(file="RICE.gif")
				self.wheat=PhotoImage(file="WHEAT2.gif")
				self.cotton=PhotoImage(file="COTTON.gif")
				self.jute=PhotoImage(file="JUTE.gif")
				self.banana=PhotoImage(file="Banana.gif")
				self.apple=PhotoImage(file="APPLES.gif")
			elif self.selected==2:
				self.rice=PhotoImage(file="RICE.gif")
				self.wheat= PhotoImage(file="WHEAT.gif")
				self.cotton=PhotoImage(file="COTTON2.gif")
				self.jute=PhotoImage(file="JUTE.gif")
				self.banana=PhotoImage(file="Banana.gif")
				self.apple=PhotoImage(file="APPLES.gif")
			elif self.selected==3:
				self.rice=PhotoImage(file="RICE.gif")
				self.wheat= PhotoImage(file="WHEAT.gif")
				self.cotton=PhotoImage(file="COTTON.gif")
				self.jute=PhotoImage(file="JUTE2.gif")
				self.banana=PhotoImage(file="Banana.gif")
				self.apple=PhotoImage(file="APPLES.gif")
			elif self.selected==4:
				self.rice=PhotoImage(file="RICE.gif")
				self.wheat= PhotoImage(file="WHEAT.gif")
				self.cotton=PhotoImage(file="COTTON.gif")
				self.jute=PhotoImage(file="JUTE.gif")
				self.banana=PhotoImage(file="BANANA2.gif")
				self.apple=PhotoImage(file="APPLES.gif")
			elif self.selected==5:
				self.rice=PhotoImage(file="RICE.gif")
				self.wheat= PhotoImage(file="WHEAT.gif")
				self.cotton=PhotoImage(file="COTTON.gif")
				self.jute=PhotoImage(file="JUTE.gif")
				self.banana=PhotoImage(file="Banana.gif")
				self.apple=PhotoImage(file="APPLES2.gif")

			image2= self.rice
			self.canvas.data["image2"]=image2
			image2=self.canvas.data["image2"]
			self.canvas.create_image(499.5, 630.5, image=image2)
			self.canvas.create_text(499.5, 640, text=str(self.numSeeds[0]), font= "Helvetica 15 bold")

			image3= self.wheat
			self.canvas.data["image3"]=image3
			image3=self.canvas.data["image3"]
			self.canvas.create_image(581.5, 630.5, image=image3)
			self.canvas.create_text(581.5, 640, text=str(self.numSeeds[1]), font= "Helvetica 15 bold")

			image4= self.cotton
			self.canvas.data["image4"]=image4
			image4=self.canvas.data["image4"]
			self.canvas.create_image(663.5, 630.5, image=image4)
			self.canvas.create_text(663.5, 640, text=str(self.numSeeds[2]), font= "Helvetica 15 bold")

			image5= self.jute
			self.canvas.data["image5"]=image5
			image5=self.canvas.data["image5"]
			self.canvas.create_image(745.5, 630.5, image=image5)
			self.canvas.create_text(745.5, 640, text=str(self.numSeeds[3]), font= "Helvetica 15 bold")

			image6= self.banana
			self.canvas.data["image6"]=image6
			image6=self.canvas.data["image6"]
			self.canvas.create_image(827.5, 630.5, image=image6)
			self.canvas.create_text(827.5, 640, text=str(self.numSeeds[4]), font= "Helvetica 15 bold")

			image7= self.apple
			self.canvas.data["image7"]=image7
			image7=self.canvas.data["image7"]
			self.canvas.create_image(909.5, 630.5, image=image7)
			self.canvas.create_text(909.5, 640, text=str(self.numSeeds[5]), font= "Helvetica 15 bold")

			self.drawFarmScreen()
			if (self.currCol!=None and self.currRow!=None):
				highlightImg= self.highlightDict[self.crop_matrix[self.currRow][self.currCol].name]
				self.canvas.data["highlightImg"]=highlightImg
				highlightImg=self.canvas.data["highlightImg"]
				self.canvas.create_image(28+94+self.currCol*189, 106+45+self.currRow*91, image=highlightImg)
			self.drawPercentages()
			self.drawRectangles()
			if (self.timeLeft<=0):
				self.farmScreen=False
				self.gameOverScreen=True

		
		elif self.marketScreen==True:
			mkt= self.marketScreenImage
			self.canvas.data["mkt"]=mkt
			mkt=self.canvas.data["mkt"]
			self.canvas.create_image(self.width/2, self.height/2, image=mkt)
			self.canvas.create_text(680, 60, text=str(self.bank.bank_balance), fill="white", font= "Helvetica 35 bold")
			self.canvas.create_text(221.5, 270, text=str(self.seed_list[0].buying_price), font= "Helvetica 20 bold")
			self.canvas.create_text(492.5, 270, text=str(self.seed_list[1].buying_price), font= "Helvetica 20 bold")
			self.canvas.create_text(221.5, 471, text=str(self.seed_list[2].buying_price), font= "Helvetica 20 bold")
			self.canvas.create_text(492.5, 471, text=str(self.seed_list[3].buying_price), font= "Helvetica 20 bold")
			self.canvas.create_text(223.5, 669, text=str(self.seed_list[4].buying_price), font= "Helvetica 20 bold")
			self.canvas.create_text(495.5, 669, text=str(self.seed_list[5].buying_price), font= "Helvetica 20 bold")


			if 185<=self.hoverX<=247 and 118<=self.hoverY<=207.1:
				plus= self.plus
				self.canvas.data["plus"]=plus
				plus = self.canvas.data["plus"]
				self.canvas.create_image(216,158.55, image=plus)
			elif 455<=self.hoverX<=517 and 116<=self.hoverY<=205.1:
				plus= self.plus
				self.canvas.data["plus"]=plus
				plus = self.canvas.data["plus"]
				self.canvas.create_image(486, 158.55, image=plus)
			elif 185<=self.hoverX<=247 and 316<=self.hoverY<=405.1:
				plus= self.plus
				self.canvas.data["plus"]=plus
				plus = self.canvas.data["plus"]
				self.canvas.create_image(216, 360.55, image=plus)
			elif 455<=self.hoverX<=517 and 316<=self.hoverY<=405.1:
				plus= self.plus
				self.canvas.data["plus"]=plus
				plus = self.canvas.data["plus"]
				self.canvas.create_image(486, 358.55, image=plus)
			elif 185<=self.hoverX<=247 and 518<=self.hoverY<=607.1:
				plus= self.plus
				self.canvas.data["plus"]=plus
				plus = self.canvas.data["plus"]
				self.canvas.create_image(216, 560.55, image=plus)
			elif 455<=self.hoverX<=517 and 518<=self.hoverY<=607.1:
				plus= self.plus
				self.canvas.data["plus"]=plus
				plus = self.canvas.data["plus"]
				self.canvas.create_image(486, 560.55, image=plus)

			##this is the animation effects for buttons
			elif 40<=self.hoverX<=175 and 148<=self.hoverY<=283:
				newRice= self.newRice
				self.canvas.data["newRice"]=newRice
				newRice = self.canvas.data["newRice"]
				self.canvas.create_image(107, 215, image=newRice)

			elif 40<=self.hoverX<=175 and 348<=self.hoverY<=483:

				newCotton= self.newCotton
				self.canvas.data["newCotton"]=newCotton
				newCotton = self.canvas.data["newCotton"]
				self.canvas.create_image(107, 415, image=newCotton)

			elif 40<=self.hoverX<=175 and 547<=self.hoverY<=682:
				
				newBanana= self.newBanana
				self.canvas.data["newBanana"]=newBanana
				newBanana = self.canvas.data["newBanana"]
				self.canvas.create_image(107, 614, image=newBanana)

			elif 311<=self.hoverX<=446 and 148<=self.hoverY<=283:
	
				newWheat= self.newWheat
				self.canvas.data["newWheat"]=newWheat
				newWheat = self.canvas.data["newWheat"]
				self.canvas.create_image(378, 215, image=newWheat)

			elif 311<=self.hoverX<=446 and 348<=self.hoverY<=483:
				
				newJute= self.newJute
				self.canvas.data["newJute"]=newJute
				newJute = self.canvas.data["newJute"]
				self.canvas.create_image(378, 415, image=newJute)

			elif 311<=self.hoverX<=446 and 547<=self.hoverY<=682:
				
				newApple= self.newApple
				self.canvas.data["newApple"]=newApple
				newApple = self.canvas.data["newApple"]
				self.canvas.create_image(378, 614, image=newApple)


			self.canvas.create_text(107.5, 246, text=str(self.numSeeds[0]), font= "Helvetica 20 bold")
			self.canvas.create_text(378.5, 246, text=str(self.numSeeds[1]), font= "Helvetica 20 bold")
			self.canvas.create_text(107.5, 446, text=str(self.numSeeds[2]), font= "Helvetica 20 bold")
			self.canvas.create_text(378.5, 446, text=str(self.numSeeds[3]), font= "Helvetica 20 bold")
			self.canvas.create_text(107.5, 645, text=str(self.numSeeds[4]), font= "Helvetica 20 bold")
			self.canvas.create_text(378.5, 645, text=str(self.numSeeds[5]), font= "Helvetica 20 bold")

		elif self.riceScreen==True:
			riceFlash= self.riceFlash
			self.canvas.data["riceFlash"]=riceFlash
			riceFlash = self.canvas.data["riceFlash"]
			self.canvas.create_image(self.width/2,self.height/2, image=riceFlash)
			self.canvas.create_text(686,307.5, text=str(self.rice1.selling_price), font="Helvetica 35 bold")

		elif self.wheatScreen==True:
			wheatFlash= self.wheatFlash
			self.canvas.data["wheatFlash"]=wheatFlash
			wheatFlash = self.canvas.data["wheatFlash"]
			self.canvas.create_image(self.width/2,self.height/2, image=wheatFlash)
			self.canvas.create_text(686,307.5, text=str(self.wheat1.selling_price), font="Helvetica 35 bold")

		elif self.cottonScreen==True:
			cottonFlash= self.cottonFlash
			self.canvas.data["cottonFlash"]=cottonFlash
			cottonFlash = self.canvas.data["cottonFlash"]
			self.canvas.create_image(self.width/2,self.height/2, image=cottonFlash)
			self.canvas.create_text(686,307.5, text=str(self.cotton1.selling_price), font="Helvetica 35 bold")

		elif self.juteScreen==True:
			juteFlash= self.juteFlash
			self.canvas.data["juteFlash"]=juteFlash
			juteFlash = self.canvas.data["juteFlash"]
			self.canvas.create_image(self.width/2,self.height/2, image=juteFlash)
			self.canvas.create_text(686,307.5, text=str(self.jute1.selling_price), font="Helvetica 35 bold")

		elif self.appleScreen==True:
			appleFlash= self.appleFlash
			self.canvas.data["appleFlash"]=appleFlash
			appleFlash = self.canvas.data["appleFlash"]
			self.canvas.create_image(self.width/2,self.height/2, image=appleFlash)
			self.canvas.create_text(686,307.5, text=str(self.apple1.selling_price), font="Helvetica 35 bold")

		elif self.bananaScreen==True:
			bananaFlash= self.bananaFlash
			self.canvas.data["bananaFlash"]=bananaFlash
			bananaFlash = self.canvas.data["bananaFlash"]
			self.canvas.create_image(self.width/2,self.height/2, image=bananaFlash)
			self.canvas.create_text(686,307.5, text=str(self.banana1.selling_price), font="Helvetica 35 bold")

		elif self.gameOverScreen==True:
			game= self.gameOverScreenImage
			self.canvas.data["game"]=game 
			game = self.canvas.data["game"]
			self.canvas.create_image(self.width/2,self.height/2, image=game)

		elif self.infoScreen==True:
			janky= self.janky
			self.canvas.data["janky"]=janky
			game = self.canvas.data["janky"]
			self.canvas.create_image(self.width/2,self.height/2, image=janky)
			
			flash= self.flashDict[self.expCrop]
			self.canvas.data["flash"]=flash
			flash = self.canvas.data["flash"]
			self.canvas.create_image(504, 494, image=flash)

			piche= self.back
			self.canvas.data["piche"]=piche
			flash = self.canvas.data["piche"]
			self.canvas.create_image(766, 269.5 , image=piche)

			self.canvas.create_text(544.5, 123.5, text=self.address, fill="white", font="Helvetica 35" )
			self.canvas.create_text(425, 195.5, text=str(self.altitude), fill="white",font="Helvetica 35 ")
			self.canvas.create_text(789, 195.5, text=str(self.temp), fill="white", font="Helvetica 35 ")
			self.canvas.create_text(697.5, 448.5, text=crop(self.expCrop).selling_price, font="Helvetica 35 ")

			sms=self.sms
			self.canvas.data["sms"]=sms
			flash = self.canvas.data["sms"]
			self.canvas.create_image(790, 66, image=sms)

			ish=self.ish
			self.canvas.data["ish"]=ish
			flash = self.canvas.data["ish"]
			self.canvas.create_image(277.5, 267, image=ish)

			if 739<=self.hoverX<=841 and 40<=self.hoverY<=93:
				sms2=self.sms2
				self.canvas.data["sms2"]=sms2
				flash = self.canvas.data["sms2"]
				self.canvas.create_image(790, 66, image=sms2)


	#increases the current time the object has been planted for 
	def incrementTime(self):
		matrix= self.crop_matrix
		for row in xrange(5):
			for col in xrange(5):
				if matrix[row][col].name!="NULL":
					matrix[row][col].current_time+=0.25

	#decreases current life of the object
	def decrementLife(self):
		matrix= self.crop_matrix
		for row in xrange(5):
			for col in xrange(5):
				if matrix[row][col].name!="NULL":
					matrix[row][col].life-=0.1

	def removeDead(self):
		matrix= self.crop_matrix
		for row in xrange(5):
			for col in xrange(5):
				if matrix[row][col].check_dead_status()==True:
					matrix[row][col]=crop("null")

	def drawRectangles(self):
		matrix= self.crop_matrix
		for row in xrange(5):
			for col in xrange(5):
				cell=matrix[row][col]
				self.canvas.create_rectangle(28 +189*col,106+91*row, 28+189*(col+1), 106+91*row+10,fill="white", width=0)
				expLength= (cell.life/cell.harvest_life)*189
				if expLength<0:
					expLength=0
				if expLength>189:
					expLength=189
				self.canvas.create_rectangle(28+189*col,106+91*row, 28+189*col+expLength, 106+91*row+10,fill="#60CFCD", width=0)



FarmGame("9920241690").run()

