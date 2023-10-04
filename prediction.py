# This is a Word prediction game
# For this first import random module
import random 
name = input ("Enter your name : ")
# Here the user is asked to enter the name first
# Give a positive welcome to the user
print ("\n") 
# '\n' used to create a new line
print ("\t GOOD LUCK !!! ", name.upper()) 
# '\t' used in representing certain whitespace characters
words =["computer","science","rainbow","waterfall","Drive",
        "answer","apple","article","assist","attack",
        "attempt","attend","attention","attitude","beach","bean",
        "bear","beat","beautiful","beauty","chairman","classic",
        "collection","correct","coverage","cultural","direction","dramatic",
        "electronic","english","familiar","female","foreign","gallery","garden",
        "horizon","ignore","justice"]
# Words from this list,the function will choose one word
word = random.choice(words)
print ("\n")
print ("Guess the characters".upper())
guesses = ' '
turns = 12
# In turns there is a limit of guesses.
# we can use any count for guesses.
# Now create while loop 
while turns > 0:
    failed = 0
# In while loop create 'for loop' 
# For identify each charachter in the random word   
    for char in word:
# Here creating  'if condition '
# For identifying guess word is correct or not         
        if char in guesses:
            print (char, end =" ") 
        else :
            print ("_") 
# Every incorrect word 1 wil be incremented               
            failed += 1
# Failed Zero means user inputed correct word
# And the game end            
    if failed == 0:
        print ("YOU WIN !!!")
        print ("\n")
        print ( "\t The word is", word) 
        break 
# If user has input the wrong alphabet then
# it will ask user to enter another alphabet         

    print()
# Here the user is asked to enter character   
    guess = input ("guess a character : ") 
# Every input character will be stored in guesses
    guesses += guess
# Check input with the character in word
    if guess not in word :
        turns -= 1  
# If the character doesn’t match the word
# Then “Wrong” will be given as output         
        print ("Worng Try another one")
# This will print the number of
# turns left for the user        
        print ( "You have", + turns, "more guesses")
        if turns == 0:      
            print("You Loose")

