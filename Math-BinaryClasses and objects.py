#creating a class (a class functions as a template for an object)

class Book:     #self is a special parameter, used to access a single instance of a class & must be included when initializing instance variables local to a method inside a class
                #class variables are shared by all instances of the class
    
    #initializing the instance variables: 
    
    def __init__(self, pBooktitle, pBookauthor, pYearpublished):    
        self._title = pBooktitle                                    #always prefix instance variables with the self. keyword 
        self.author = pBookauthor                                   #these are the instance variables. The underscore before title is a convention.
        self.year = pYearpublished                                  #It warns coders not to directly access the variable because it has associated limiting properties.
        print ('creating a book file')

    def __str__ (self):
        return "Book Title: %s, Author: %s, Year Published: %d" %(self._title, self.author, self.year)
      
    #a procedure insisde a class is referred to as a method
    def calculateBookAge (self):
         self.age = 2018 - self.year
         return self.age

#to create an object in this class:
    
Book1 = Book ('Foundation', 'Asimov', 1948)                         #Python automatically includes the hidden self parameter
#The program returns 'creating a book file'

print (Book1)
#The program returns 'Book Title: Foundation, Author: Asimov, Year Published: 1946'

#to call the calculateBookAge method

Book1.calculateBookAge ()                                           #don't forget the parentheses
#The program returns 70

#To update any of the variables:
Book1.year = 1950
Book1.title = 'Foundation and Empire' 


#Adding properties:                                                 #Here I am pre-defining argument options for an instance variable
  
    @property                                                       #@property assigns a method to self.title (hidden procedure) 
    def title (self):                                               #NB: I don't totally get what is going on here yet. 
        print ('Fetching value')
        return self._title

    @title.setter                                                   #setter method: .setter is a pre-defined attribute to the property object
    def title (self, knownBook):
        if knownBook == 'Foundation' or knownBook == 'The Martian Way' or knownBook == 'Caves of Steel':
            self._title = knownBook
        else:
            print ('Are you sure he wrote that book? No changes made')


#instance, class and static methods compared:


class MethodDemo:
    a = 10                                                            #assign 10 to class variable a

    def __init__(self, pNum):
        self.num = pNum
        print ('new instance variable created with num = ', self.num)
        
    def instanceMethod (self):                                        #instance methods work with specific class instances and access them through the self parameter
         self.sum = 10 - self.num
         print (self.sum)

    @classmethod                                                      #class methods cannot access single class instances
    def classM (cls):                                                 #they have access to the class variables, via cls
        print ('Class Method. cls.a = ', cls.a)

    @staticmethod                                                     #static methods cannot access class instances or class variables
    def staticM ():                                                   #they work like any function but belong to the class namespace
        print ('Static method demo')

    
#creating the class instances
md1 = MethodDemo (3)
md2 = MethodDemo (4)

#two different ways to call each method
MethodDemo.instanceMethod (md2)
md1.instanceMethod ()

MethodDemo.classM ()
md2.classM ()

MethodDemo.staticM ()
md2.staticM ()

#The program returns:
new instance variable created with num =  3
new instance variable created with num =  4
6
7
Class Method. cls.a =  10
Class Method. cls.a =  10
Static method demo

#Many developers use only instance methods, however class and static methods can help show your intent regarding the class design
        
        
 
