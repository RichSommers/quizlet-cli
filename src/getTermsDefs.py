from src.getSet import get
import re


def find(r,t): # regex,text
	return re.findall(r,t)

def fix(text):
	return text.replace('&quot;','"')
def getInfo(link):
	text=get(link)
	#title finding
	titleRegex='(?<=title>)(.*)(?=\| Quizlet)'

	title=find(titleRegex,text)[0]

	termRegex='(?<=TermText notranslate lang-en">)(.*?)(?=<\/span)'

	TsAndDs=find(termRegex,text) #terms and defs

	organized=[]
	for i in range(0,len(TsAndDs),2):
		organized.append((fix(TsAndDs[i]),fix(TsAndDs[i+1])))
	return title, organized

if __name__=='__main__':
	testSets=['https://quizlet.com/17441448/biology-chapter-8-photosynthesis-flash-cards/','https://quizlet.com/22488198/romeo-and-juliet-flash-cards/']


	title, both = getInfo(testSets[0])
	print(title)

	for i in both:
		print(i)
