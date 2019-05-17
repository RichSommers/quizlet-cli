from getTermsDefs import getInfo
import os
from getch import _Getch
from time import sleep
from colorama import Fore,Back
import sys

#oponing set

sets=open(SETFILE,'r').read().split()


if '-n' in sys.argv:
	p=sys.argv.index('-n')
	setToGet=sets[int(sys.argv[p+1])]
else:
	setToGet=sets[0]

if '-h' in sys.argv:
	print('A command line quizlet )



print("Getting Set...")
title,cards=getInfo(setToGet)

print("Got set")


cards.append(('LAST CARD','LAST CARD'))


get=_Getch()

def clear():
	os.system('clear')

def drawWindow(text,title):
	height,width=os.popen('stty size','r').read().split()
	width=int(width)
	height=int(height)
	clear()
	tText=' '*int(width/2-len(title)/2)+'========'+title+'======='+' '*(int(width/2-len(title)/2)-int(16+len(title)/5))   # fix this mess
	sText=' '*int(width/2-len('QUIZLET')/2)+'========'+'QUIZLET'+'======='+' '*(int(width/2-len('QUIZLET')/2)-14) # website text

	print(Back.BLUE)
	print('='*width)
	print(tText)
	print(sText)
	print('='*width)
	print('\n'*int(height/5))
	print(Back.BLACK)

	print(' '*int(width/2-len(text)/2)+text)

	print('\n'*int(height/3))


cI=0 #card index
cS=DEFAULT_SIDE #card side

cng=1

while 1:

	c=str(get())

	if c==QUIT:
		break
	elif c==FLIPUP or c==FLIPDOWN:
		cS=int(not cS)
		cng=1
	elif c==NEXT:
		if cI != len(cards)-1:
			cI=cI+1
			cS=DEFAULT_SIDE
			cng=1
	elif c==LAST:
		if cI != 0:
			cI=cI-1
			cS=DEFAULT_SIDE
			cng=1
	if cng==1:
		drawWindow(cards[cI][cS],title)
	cng=0

	sleep(0.01)
