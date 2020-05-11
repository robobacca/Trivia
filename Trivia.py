import random
import time

def correct_answer(answer): #so that this chunk of code does not have to be repeated for each question  #to keep track of the number of correct questions
    correct = 'Gooc job! You got it right!\n'  #texts for a correct and wrong answer
    wrong = 'sorry, your answer was incorrect, the correct answer was'
    if q == 'An atom contains protons, neutrons and _______.':  #to determine the correct answer for each question
        if answer == 'electrons':
            return correct
        else:
            return wrong,'electrons\n'
    elif q == 'World War 2 ended in year _____.':
        if answer == '1945':
            return correct
        else:
            return wrong,'1945\n'
    elif q == 'What is the chemical symbol for oxygen ?(u)':
        if answer == 'O':
            return correct
        else:
            return wrong,'O\n'
    elif q == 'What is the point in a black hole where light cannot escape called?':
        if answer == 'event horizon':
            return correct
        else:
            return wrong,'event horizon\n'
    elif q == 'What is the prefix allocated to the word "undeserved"?':
        if answer == 'un':
            return correct
        else:
            return wrong,'un\n'
    elif q == 'In which year was YouTube created?':
        if answer == '2005':
            return correct
        else:
            return wrong,'2005\n'
    elif q == 'PVC is an acronym for the compund _____.':
        if answer == 'polyvinyl chloride':
            return correct
        else:
            return wrong,'polyvinyl chloride\n'
    elif q == 'What is the exact value of the speed of light in m/h?':
        if answer == '299792458':
            return correct
        else:
            return wrong,'299792458\n'
    elif q == 'In which year was the Sony Walkman released?':
        if answer == '1979':
            return correct
        else:
            return wrong,'1979'
    elif q == 'What is the tallest building as of 2020? (Capitalise the name)':
        if answer == 'Burj Khalifa':
            return correct
        else:
            return wrong,'Burj Khalifa'
    elif q == 'A gene mutation can cause _____ if not stopped by the kill switch of the mutated cell.':
        if answer == 'cancer':
            return correct
        else:
            return wrong,'cancer'
    elif q == 'Glucose, the simplest form of sugar, consists of 12 hydrogen atoms, 6 oxygen atoms, and 6 _____ atoms in each molecule.':
        if answer == 'carbon':
            return correct
        else:
            return wrong,'carbon'
    elif q == 'Although both graphite and carbon are made of carbon, graphite has a hexagonal layer structure wile diamond has a _____ structure.':
        if answer == 'tetrahedral':
            return correct
        else:
            return wrong,'tetrahedral'
    elif q == 'When first moon landing with a human was in _____.':
        if answer == '1969':
            return correct
        else:
            return wrong,'1969'
    elif q == 'The World Trade Centre fell in the year _____.':
        if answer == '2001':
            return correct
        else:
            return wrong,'2001'
    elif q == 'Increasing the frequency of a sound wave increases the _____ of the sound.':
        if answer == 'pitch':
            return correct
        else:
            return wrong,'pitch'
    elif q == 'What causes black holes to decay over time?':
        if answer == 'hawking radiation':
            return correct
        else:
            return wrong,'hawking radiation'
    elif q == 'Who wrote the famous book 'The Da Vinci Code'? (Capitalise the name)':
        if answer == 'Dan Brown':
            return correct
        else:
            return wrong,'Dan Brown'
    elif q == 'In the Hunger Games series, who was the original tribute for the first games shown in the book and movie? (Capitalised first name only)':
        if answer == 'Primrose':
            return correct
        else:
            return wrong,'Primrose'
    elif q == 'In Star Wars, what was the colour of Mace Windu's lightsaber?':
        if answer == 'purple':
            return correct
        else:
            return wrong,'purple'

    
    
    
print('Welcome to trivia')
print('All answers to be typed in lowercase unless question has (u) at the end')
print('There will be a total of 10 questions')
start = str(input('Please type \"begin\" to start and \"cancel\" to cancel\n')) #getting user's approval to start
if start == 'begin':
    with open("question_list.txt") as temptxt:  #to open and read the text in the .txt file
        templist = temptxt.read()
        templist2 = templist.split(';')
        qlist = [i.strip('\n') for i in templist2]  #to convert the questions into a list, and removing unwanted characters
        random.shuffle(qlist)   #randomize the questions to reduce chance of cheating
        score = 0
        start = time.time() #to start the timer
        #Question 1
        q = qlist[0]
        print('Question 1:',q)
        user_answer = str(input(''))  #getting user's answer for the question
        print(correct_answer(user_answer))  #check and display if user got the question right or wrong
        if 'job!' in correct_answer(user_answer).split(' '):
            score +=1
        #Question 2
        q = qlist[1]
        print('Question 2:',q)
        user_answer = str(input(''))
        print(correct_answer(user_answer))
        if 'job!' in correct_answer(user_answer).split(' '):
            score +=1
        #Question 3
        q = qlist[2]
        print('Question 3:',q)
        user_answer = str(input(''))
        print(correct_answer(user_answer))
        if 'job!' in correct_answer(user_answer).split(' '):
            score +=1
        #Question 4
        q = qlist[3]
        print('Question 4:',q)
        user_answer = str(input(''))
        print(correct_answer(user_answer))
        if 'job!' in correct_answer(user_answer).split(' '):
            score +=1
        #Question 5
        q = qlist[4]
        print('Question 5:',q)
        user_answer = str(input(''))
        print(correct_answer(user_answer))
        if 'job!' in correct_answer(user_answer).split(' '):
            score +=1
        #Question 6
        q = qlist[5]
        print('Question 6:',q)
        user_answer = str(input(''))
        print(correct_answer(user_answer))
        if 'job!' in correct_answer(user_answer).split(' '):
            score +=1
        #Question 7
        q = qlist[6]
        print('Question 7:',q)
        user_answer = str(input(''))
        print(correct_answer(user_answer))
        if 'job!' in correct_answer(user_answer).split(' '):
            score +=1
        #Question 8
        q = qlist[7]
        print('Question 8:',q)
        user_answer = str(input(''))
        print(correct_answer(user_answer))
        if 'job!' in correct_answer(user_answer).split(' '):
            score +=1
        #Question 9
        q = qlist[8]
        print('Question 9:',q)
        user_answer = str(input(''))
        print(correct_answer(user_answer))
        if 'job!' in correct_answer(user_answer).split(' '):
            score +=1
        #Question 10
        q = qlist[9]
        print('Question 10:',q)
        user_answer = str(input(''))
        print(correct_answer(user_answer))
        if 'job!' in correct_answer(user_answer).split(' '):
            score +=1
        end = time.time()   #end timer
        s = end - start
        m = 0
        if s == 60:
            m += 1
            s = 0
        print('Your time is',m,'minutes and','{:.2f}'.format(s),'seconds')
        print('Your score is',str(score) + '. Good effort!')
elif start == 'cancel':
    print('Program cancelled.')
else:
    print('Invalid input. Please try again.')
            
        
    
        


