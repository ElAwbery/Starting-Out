#three key functions for Math2 game.

def printInstructions (printInstructionArg):
    print (printInstructionArg)

def getUserScore (userName):                       
    try:
        scoresAccess=open ('userScores.txt', 'r')
        for line in scoresAccess:
            content = line.split (',')
            if content [0]== '%s' %(userName):      #don't need to use % here, userName can be argument   
                scoresAccess.close ()
                return content[1] 
        else:
            scoresAccess.close ()
            return '-1'

    except IOError:
        newScoresWrite=open ('UserScores.txt', 'w')
        print ('We are making you a scores file.')
        newScouresWrite.close ()                    #ALWAYS RETURN VALUES AFTER CLOSING FILES.The return function terminates execution of 
        return '-1'                                 #the procedure

                        

from os import (remove, rename)

def updateUserScore (newUser, userName, score):
    
    if newUser:
        f = open ('userScores.txt', 'a')            #outputFile would be a better name for variable
        f.write (userName + ',' +score + '\n')      #single letter variables cause problems as you forget what
        f.close ()                                  #they were referring to.
    else:
        temp = open ('userScores.tmp', 'w')
        g = open ('userScores.txt', 'r')            #inputFile better variable name
        for line in g:
            content = line.split (',')
            if content [0] == userName:
                content = (userName, score)
                temp.write (userName + ',' + score + '\n') 
            else: temp.write (line)

    temp.close ()
    g.close ()

    remove ('userScores.txt')
    rename ('userScores.tmp', 'userScores.txt')
                 



