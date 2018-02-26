#three classes for math2 game

class Game:
    def __init__(self, noOfQuestions = 0):
        self._noOfQuestions = noOfQuestions

    @property
    def noOfQuestions (self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions (self, value):
        if value < 1:
            self._noOfQuestions = 1
            print ("\nMinimum number of questions = 1", "\nHence, number of questions will be set to 1.")
        elif value > 10:
            self._noOfQuestions = 10
            print ("\nMaximum number of questions = 10", "\nHence number of questions will be set to 10.")
        else:
            self._noOfQuestions = value


class BinaryGame (Game):
    def generateQuestions (self):
        from random import randint
        score = 0
        
        for i in range (self.noOfQuestions):
            base10 = randint (1, 100)
            userResult = input ("\nPlease convert %d to binary: " %(base10))
            while True:
                try:
                    answer = int (userResult, base = 2)
                    if answer == base10:
                        score += 1
                        print ("correct")
                        break
                    else:
                        print ("Incorrect. The answer is {:b}.".format (base10))
                        break
                except:
                    print ("That was not a binary number. Try again.")
                    userResult = input ('convert', base10, 'to binary')
                    
        return score

class MathGame (Game):
    def generateQuestions (self):
        from random import randint
        score = 0
        numberList = [0, 0, 0, 0, 0]
        symbolList = ['','','','','']
        operatorDict = {1:"+", 2:"-", 3:"*", 4:"**"}

        for i in range (self.noOfQuestions):     #for each question until none left
            for index in range (0, 5):
                numberList[index] = randint (1, 9)      #randomly pick an integer, loop this 5 times through numberList
                
            for index in range (0, 4):
                if index > 0 and symbolList[index-1] == '**':
                    symbolList[index] = operatorDict[randint (1, 3)]
                else: 
                    symbolList[index]=operatorDict[randint (1,4)]

            questionString = str (numberList [0])
            
            for index in range (0, 4):
                questionString = questionString + symbolList[index] + str(numberList[index+1])
            
            result = eval(questionString)
            questionString = questionString.replace('**', '^')
            userResult = input ('Evaluate the following:%s' %(questionString))
        
            while True:
                try:
                    answer = int (userResult)
                    if answer == result:
                        score = score + 1
                        print ('Correct.')
                        break
                    else:
                        print ('Wrong! Correct answer is', result)
                        break
                except:
                    print ('ofgs, that was not even an integer. Please try harder.')
                    userResult = input ('Evaluate the following:', questionString)

        return (score)
            
                     





























        
                    
   
