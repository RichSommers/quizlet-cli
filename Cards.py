
from src.getTermsDefs import getInfo
import os
from src.getch import _Getch
from time import sleep
from colorama import Fore,Back
import sys
import random #for shuffling

#help option
if '-h' in sys.argv or '--help' in sys.argv:
	print('\n\nA command line quizlet thingy')
	print('-n # for selecting set from sets.txt\n\n')
	print('-s or --shuffle for shuffling the order of the cards')
	sys.exit(0)


#opening conf file      quizlet-cli.conf
options=open('quizlet-cli.conf','r').read().split('\n')

i=0
while i < len(options):
	if '#' in options[i]:
		del options[i]
		i=i-1
	i=i+1


DEFAULT_SIDE=int(options[0])
NEXT=options[1]
LAST=options[2]
FLIPUP=options[3]
FLIPDOWN=options[4]
QUIT=options[5]
SETFILE=options[6]


#oponing set

sets=open(SETFILE,'r').read().split()
if '-n' in sys.argv:
	p=sys.argv.index('-n')
	setToGet=sets[int(sys.argv[p+1])-1]
else:
	setToGet=sets[0]
if '-s' in sys.argv or '--shuffle' in sys.argv:
	shuffle=True
else:
	shuffle=False
if '--default-side' in sys.argv:
	p=sys.argv.index('--default-side')
	DEFAULT_SIDE = int(sys.argv[p+1])
elif '-df' in sys.argv:
	p=sys.argv.index('-df')
	DEFAULT_SIDE = int(sys.argv[p+1])

print("Getting Set...")
title,cards=getInfo(setToGet)
print("Got set")


'''
def fix(text):   #can be done better if done in getInfo
	return text.replace('&quot;','"')  #maybe \"
for i in title:
	for j in i:
		j=fix(j)
for i in cards:
	for j in i:
		j=fix(j)

'''
if shuffle:
	random.shuffle(cards)

cards.append(('LAST CARD','LAST CARD'))


get=_Getch()

def clear():
	os.system('clear')

def drawWindow(text,title):
	height,width=os.popen('stty size','r').read().split()
	width=int(width)
	height=int(height)
	clear()
	tText=' '*int(width/2-len(title)/2)+'========'+title+'======='+' '*(int(width/2-len(title)/2)-int(16+len(title)/5)+12)   # fix this mess
	sText=' '*int(width/2-len('QUIZLET')/2)+'========'+'QUIZLET'+'======='+' '*(int(width/2-len('QUIZLET')/2)-15) # website text

	print(Back.BLUE)
	print('='*width)
	print(tText)
	print(sText)
	print('='*width)
	print('\n'*int(height/5))
	print(Back.BLACK)

	print(' '*int(width/2-len(text)/2)+text)

	print('\n'*int(height/3))
	print('('+str(cI+1)+'/'+str(len(cards))+')')

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

