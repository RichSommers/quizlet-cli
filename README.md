<h1>quizlet-cli</h1>
A command line version of quizlet
Works on Linux and maybe windows(untested). 

<hl>
  Usage:
  Put the url(s) of the quizlet sets you wish to study in the sets.txt file.
 <code> python3 Cards.py </code>
 will select the first set in the sets.txt.
 
 
 <code> python3 Cards.py -h </code>
 Will display limited help options and exit.
 
  <code> python3 Cards.py -n X </code>
  Where X is the number of the line of the set from sets.txt starting from 1. 
   <code> python3 Cards.py -s </code>
  Will run the flashcards but shuffled. 
  
  You can combine -n and -s without a problem but not -h
  
   <code> python3 Cards.py -h -n 1 </code>



Configuration:

keys are stored in quizlet-cli.conf

default
next  l
previous j
flip up i
flip down k   flip up and flip down do the same thing for now
quit q    Because of the way it gets characters for flipping ctrl-c or ctrl-z will not work once the set is loaded
