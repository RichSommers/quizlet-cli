from src.getSet import get
from colorama import Fore,Back
import os
from math import ceil as cl #for headers
import re

#CONFIG
SETS_DISPLAYED=5

def clear():
	os.system('clear')

bb= Back.BLUE #baack blue
bbl=Back.BLACK # back black

height,width=os.popen('stty size','r').read().split()
w=int(width)
h=int(height)

print(w,h)

site='Quizlet' # for length
def showTitle():
	print(bb+'='*w)
	print('='*(cl(w/2)-cl(len(site))+1)+site+'='*(cl(w/2)-cl(len(site)/2)+2))
	print('='*w+bbl)

def getSetNames(searchText):
	text=get('https://quizlet.com/subject/'+searchText)
	namesRegex='(?<=cardHeaderTitle">)(.*?)(?=</span)'
	names=re.findall(namesRegex,text)
	linksRegex='(?<=data-sourcename="" href=")(.*?)(?=")'
	links=re.findall(linksRegex,text)
	return names,links

#drawing loop
clear()
showTitle()
c=input('Search:  ')

while c!='q':
	clear()
	showTitle()
	print("Loading....")
	ns,ls=getSetNames(c)  # names, links
	ns=ns[0:SETS_DISPLAYED]
	ls=ls[0:SETS_DISPLAYED]
	clear()
	showTitle()
	print('Select the set you want to be added to your sets.')
	for i in range(len(ns)):
		print(Fore.BLACK+Back.WHITE+str(i+1)+'.'+Fore.WHITE+Back.BLACK+'  '+ns[i])
	print('0. Do Nothing')
	sN=int(input('Set Number?  '))
	if sN!=0:
		currentSets=open('sets.txt','r+')
		amtOfSets=len(currentSets.read().split('\n'))
		currentSets.write(ls[sN]+'\n') #write next link to file maybe only works because of weird/intended r+ behaviour
		print('Link added as link #'+str(amtOfSets))
		wait=input('Press any key when ready')
	clear()
	showTitle()
	c=input('\nSearch:  ')
