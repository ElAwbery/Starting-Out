from MyGameTasks import printInstructions, getUserScore, updateUserScore
from MyGameClasses import Game, MathGame, BinaryGame

try:
    #declare variables
    mathInstructions = '''
In this game, you will be given a simple arithmetic question.
Each correct answer gives you one mark.
No mark is deducted for wrong answers.
'''
    binaryInstructions = '''
In this game, you will be given a number in base 10.
Your task is to convert this number to base 2.
Each correct answer gives you one mark.
No mark is deducted for wrong answers.
'''
    bg = BinaryGame ()
    mg = MathGame ()
    
    userName = input ('\nUsername pls:')
    
    score = int(getUserScore (userName))
    
    if score == -1:
         newUser = True
         score = 0
    else:
        newUser = False

    print ('Hello', userName, 'Let\'s go! \nYour score is', score)
                              
    #use a while loop to run the program until the user chooses to exit
    
    userChoice = 0
    
    while userChoice != '-1':

        game = input ('Math game (1) or Binary game (2)?')
       
        while game != '1' and game != '2':
            game = input ('Type 1 if you want to play the math game, or type 2 if you want to play the binary game.')
            
        numPrompt = input ('How many questions do you want per game, (1 to 10)?')
        while True:
            try:
                num = int(numPrompt) 
                break
            except:
                print ('That was not a valid number from 1 to 10')
                numPrompt = input ('Try again. Chhose a number from 1 to 10.')

        if game == '1':
            mg.noOfQuestions = num
            printInstructions (mathInstructions)
            score = score + mg.generateQuestions ()
        else:
            bg.noOfQuestions = num
            printInstructions (binaryInstructions)
            score = score + bg.generateQuestions ()
        break
                             
    #update the user's score after they exit the program
    updateUserScore (newUser, userName, str(score))

except Exception as e:
    #inform users that an error has occurred and the program will exit
    print ('Something has gone horribly wrong. Sorry about that. Exiting program.')
    print ('Eror:', e)
        

























