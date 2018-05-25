from graphics import *
from random import *
win = GraphWin(width=600,height=400)

#win.setBackground(color_rgb(128,80,53))

PlCards=Rectangle(Point(100,50),Point(200,200))
CmpCards=Rectangle(Point(400,50),Point(500,200))
Start=Rectangle(Point(250,75),Point(350,150))
Reset=Rectangle(Point(275,175),Point(325,200))
PlScore=Rectangle(Point(100,250),Point(200,300))
CmpScore=Rectangle(Point(400,250),Point(500,300))

# draw rectangles as buttons...

StartMessage=Text(Point(300,112.5),"START")
ResetMessage=Text(Point(300,187.5),"RESET")
TitleMessage=Text(Point(300,50),"WAR")
# draw  text inside the boxes

IdPlMessage=Text(Point(150,45),"You")
IdCmpMessage=Text(Point(450,45),"Computer")
ScorePlMessage=Text(Point(150,245),"Score")
ScoreCmpMessage=Text(Point(450,245),"Score")
# draw more text in the boxes

TitleMessage.setSize(36)

CmpCards.draw(win)
PlCards.draw(win)
Start.draw(win)
PlScore.draw(win)
CmpScore.draw(win)
# call the functions.   

StartMessage.draw(win)
TitleMessage.draw(win)
IdPlMessage.draw(win)
IdCmpMessage.draw(win)
ScorePlMessage.draw(win)
ScoreCmpMessage.draw(win)

#win.setBackground("green")

PlayerList=0
CompList=0
List1=["Ace Spades","Ace Hearts","Ace Diamonds","Ace Clubs","King Spades","King Hearts","King Diamonds","King Clubs","Queen Spades","Queen Hearts","Queen Diamonds","Queen Clubs","Jack Spades","Jack Hearts","Jack Diamonds","Jack Clubs","10 Spades","10 Hearts","10 Diamonds","10 Clubs","9 Spades","9 Hearts","9 Diamonds","9 Clubs","8 Spades","8 Hearts","8 Diamonds","8 Clubs","7 Spades","7 Hearts","7 Diamonds","7 Clubs","6 Spades","6 Hearts","6 Diamonds","6 Clubs","5 Spades","5 Hearts","5 Diamonds","5 Clubs","4 Spades","4 Hearts","4 Diamonds","4 Clubs","3 Spades","3 Hearts","3 Diamonds","3 Clubs","2 Spades","2 Hearts","2 Diamonds","2 Clubs"]

def runGame():
	p=0
	PlScore=0
	CmpScore=0
	List1=["Ace Spades","Ace Hearts","Ace Diamonds","Ace Clubs","King Spades","King Hearts","King Diamonds","King Clubs","Queen Spades","Queen Hearts","Queen Diamonds","Queen Clubs","Jack Spades","Jack Hearts","Jack Diamonds","Jack Clubs","10 Spades","10 Hearts","10 Diamonds","10 Clubs","9 Spades","9 Hearts","9 Diamonds","9 Clubs","8 Spades","8 Hearts","8 Diamonds","8 Clubs","7 Spades","7 Hearts","7 Diamonds","7 Clubs","6 Spades","6 Hearts","6 Diamonds","6 Clubs","5 Spades","5 Hearts","5 Diamonds","5 Clubs","4 Spades","4 Hearts","4 Diamonds","4 Clubs","3 Spades","3 Hearts","3 Diamonds","3 Clubs","2 Spades","2 Hearts","2 Diamonds","2 Clubs"]
	while p<26:
	
		aPoint=win.getMouse()

		ClickX=int(aPoint.getX())
		ClickY=int(aPoint.getY())
		p=p+1

		if p>1:
			Score1.undraw()
			Score2.undraw()

			PlCardTop.undraw()
			CmpCardTop.undraw()

		if 249<ClickX<351 and 74<ClickY<151 and (p)%2==randint(0,1):
			

			x=int(randint(0,(53-(2*int(p)))))
			PlCard=List1[x]
			List1=List1[:(x)]+List1[(x+1):]
			y=int(randint(0,(52-(2*int(p)))))
			CmpCard=List1[y]
			List1=List1[:(y)]+List1[(y+1):]
			print str(x) + " " + str(y)
			if x<=y:
				PlScore=str(int(PlScore)+1)
			else:
				CmpScore=str(int(CmpScore)+1)

			Score1=Text(Point(150,275),PlScore)
			Score2=Text(Point(450,275),CmpScore)

			Score1.draw(win)
			Score2.draw(win)

			a=PlCard.find(" ")
			b=CmpCard.find(" ")

			if PlCard[0]=="1":
				PlCardTop=Text(Point(130,68),"10")
				PlCardTop2=Text(Point(170,186),"10")
			else:
				PlCardTop=Text(Point(130,68),str(PlCard[0]))
				PlCardTop2=Text(Point(170,186),str(PlCard[0]))

			if CmpCard[0]=="1":
				CmpCardTop=Text(Point(430,68),"10")
				CmpCardTop2=Text(Point(470,186),"10")	
			else:
				CmpCardTop=Text(Point(430,68),str(CmpCard[0]))
				CmpCardTop2=Text(Point(470,186),str(CmpCard[0]))

			if str(PlCard[a+1]) == "H":
				PlCardTop.setTextColor("red")
			elif str(PlCard[a+1]) == "D":
				PlCardTop.setTextColor("red")
			else:
				PlCardTop.setTextColor("black")

			if str(CmpCard[b+1]) == "H":
				CmpCardTop.setTextColor("red")
			elif str(CmpCard[b+1]) == "D":
				CmpCardTop.setTextColor("red")
			else:
				CmpCardTop.setTextColor("black")

			if str(PlCard[a+1]) == "H":
				PlCardTop2.setTextColor("red")
			elif str(PlCard[a+1]) == "D":
				PlCardTop2.setTextColor("red")
			else:
				PlCardTop2.setTextColor("black")

			if str(CmpCard[b+1]) == "H":
				CmpCardTop2.setTextColor("red")
			elif str(CmpCard[b+1]) == "D":
				CmpCardTop2.setTextColor("red")
			else:
				CmpCardTop2.setTextColor("black")



			if str(PlCard[a+1]) == "H":
				image1=Image(Point(150,125), "heart.gif")
			elif str(PlCard[a+1]) == "D":
			 	image1=Image(Point(150,125), "diamond.gif")
			elif str(PlCard[a+1]) == "S":
			 	image1=Image(Point(150,125), "spade.gif")
			else:
			 	image1=Image(Point(150,125), "club.gif")

			if str(CmpCard[b+1]) == "H":
			 	image2=Image(Point(450,125), "heart.gif")
			elif str(CmpCard[b+1]) == "D":
			 	image2=Image(Point(450,125), "diamond.gif")
			elif str(CmpCard[b+1]) == "S":
			 	image2=Image(Point(450,125), "spade.gif")
			else:
			 	image2=Image(Point(450,125), "club.gif")

			image1.draw(win)
			image2.draw(win)

			
			PlCardTop.setSize(30)
			CmpCardTop.setSize(30)

			PlCardTop.draw(win)
			CmpCardTop.draw(win)

			PlCardTop2.setSize(30)
			CmpCardTop2.setSize(30)

			PlCardTop2.draw(win)
			CmpCardTop2.draw(win)
		elif 249<ClickX<351 and 74<ClickY<151:

			y=int(randint(0,(53-(2*int(p)))))
			CmpCard=List1[y]
			List1=List1[:(y)]+List1[(y+1):]
			x=int(randint(0,(52-(2*int(p)))))
			PlCard=List1[x]
			List1=List1[:(x)]+List1[(x+1):]
			print str(x) + "." + str(y)
			if x<y:
				PlScore=str(int(PlScore)+1)
			else:
				CmpScore=str(int(CmpScore)+1)

			Score1=Text(Point(150,275),PlScore)
			Score2=Text(Point(450,275),CmpScore)

			Score1.draw(win)
			Score2.draw(win)

			a=PlCard.find(" ")
			b=CmpCard.find(" ")

			if PlCard[0]=="1":
				PlCardTop=Text(Point(130,68),"10")
				PlCardTop2=Text(Point(170,186),"10")
			else:
				PlCardTop=Text(Point(130,68),str(PlCard[0]))
				PlCardTop2=Text(Point(170,186),str(PlCard[0]))

			if CmpCard[0]=="1":
				CmpCardTop=Text(Point(430,68),"10")
				CmpCardTop2=Text(Point(470,186),"10")	
			else:
				CmpCardTop=Text(Point(430,68),str(CmpCard[0]))
				CmpCardTop2=Text(Point(470,186),str(CmpCard[0]))

			if str(PlCard[a+1]) == "H":
				PlCardTop.setTextColor("red")
			elif str(PlCard[a+1]) == "D":
				PlCardTop.setTextColor("red")
			else:
				PlCardTop.setTextColor("black")

			if str(CmpCard[b+1]) == "H":
				CmpCardTop.setTextColor("red")
			elif str(CmpCard[b+1]) == "D":
				CmpCardTop.setTextColor("red")
			else:
				CmpCardTop.setTextColor("black")

			if str(PlCard[a+1]) == "H":
				PlCardTop2.setTextColor("red")
			elif str(PlCard[a+1]) == "D":
				PlCardTop2.setTextColor("red")
			else:
				PlCardTop2.setTextColor("black")

			if str(CmpCard[b+1]) == "H":
				CmpCardTop2.setTextColor("red")
			elif str(CmpCard[b+1]) == "D":
				CmpCardTop2.setTextColor("red")
			else:
				CmpCardTop2.setTextColor("black")



			if str(PlCard[a+1]) == "H":
				image1=Image(Point(150,125), "heart.gif")
			elif str(PlCard[a+1]) == "D":
			 	image1=Image(Point(150,125), "diamond.gif")
			elif str(PlCard[a+1]) == "S":
			 	image1=Image(Point(150,125), "spade.gif")
			else:
			 	image1=Image(Point(150,125), "club.gif")

			if str(CmpCard[b+1]) == "H":
			 	image2=Image(Point(450,125), "heart.gif")
			elif str(CmpCard[b+1]) == "D":
			 	image2=Image(Point(450,125), "diamond.gif")
			elif str(CmpCard[b+1]) == "S":
			 	image2=Image(Point(450,125), "spade.gif")
			else:
			 	image2=Image(Point(450,125), "club.gif")

			image1.draw(win)
			image2.draw(win)

			
			PlCardTop.setSize(30)
			CmpCardTop.setSize(30)

			PlCardTop.draw(win)
			CmpCardTop.draw(win)

			PlCardTop2.setSize(30)
			CmpCardTop2.setSize(30)

			PlCardTop2.draw(win)
			CmpCardTop2.draw(win)


	if int(PlScore)<int(CmpScore) :
		EndMessage=Text(Point(100,20),"You lost!")
	elif int(CmpScore)<int(PlScore) :
		EndMessage=Text(Point(100,20),"You won!")
	else:
		EndMessage=Text(Point(100,20),"It's a tie!")

	EndMessage.setSize(36)
	EndMessage.draw(win)

	Reset.draw(win)
	ResetMessage.draw(win)

	#Score1.undraw()
	#Score2.undraw()

	#PlCardTop.undraw()
	#CmpCardTop.undraw()

	



runGame()

#aPoint=win.getMouse()

#ClickX=int(aPoint.getX())
#ClickY=int(aPoint.getY())

x=1
while x>0:
	aPoint=win.getMouse()

	ClickX=int(aPoint.getX())
	ClickY=int(aPoint.getY())
	if 274<ClickX<326 and 175<ClickY<201:

		win.close()

		win = GraphWin(width=600,height=400)

		#win.setBackground(color_rgb(128,80,53))

		PlCards=Rectangle(Point(100,50),Point(200,200))
		CmpCards=Rectangle(Point(400,50),Point(500,200))
		Start=Rectangle(Point(250,75),Point(350,150))
		Reset=Rectangle(Point(275,175),Point(325,200))
		PlScore=Rectangle(Point(100,250),Point(200,300))
		CmpScore=Rectangle(Point(400,250),Point(500,300))

		# draw rectangles as buttons...

		StartMessage=Text(Point(300,112.5),"START")
		ResetMessage=Text(Point(300,187.5),"RESET")
		TitleMessage=Text(Point(300,50),"WAR")
		# draw  text inside the boxes

		IdPlMessage=Text(Point(150,45),"You")
		IdCmpMessage=Text(Point(450,45),"Computer")
		ScorePlMessage=Text(Point(150,245),"Score")
		ScoreCmpMessage=Text(Point(450,245),"Score")
		# draw more text in the boxes

		TitleMessage.setSize(34)

		CmpCards.draw(win)
		PlCards.draw(win)
		Start.draw(win)
		PlScore.draw(win)
		CmpScore.draw(win)
		# call the functions.   

		StartMessage.draw(win)
		TitleMessage.draw(win)
		IdPlMessage.draw(win)
		IdCmpMessage.draw(win)
		ScorePlMessage.draw(win)
		ScoreCmpMessage.draw(win)

		p=0
		x=x
		runGame()


win.getMouse()













