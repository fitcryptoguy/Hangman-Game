import random
from hangman_art import stages, logo
from hangman_words import word_list, l2
from replit import clear
#______________________________________________________________GAME START__________________________________________________________________________________
print("""" 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
""")


#1choosing a random word
orignal_word = random.choice(l2)async
#____________________________________________________________________________________________________________________________________________________________
# creating a list of "_" blank items
display = []
for letter in orignal_word:
    display.append("_")
print(display)

#creating lives
lives = len(orignal_word)



#__________________________________________________________________________________________________________________________________________________________

#take input from user and reveal the user guess if it's present in the orignal word. We eneed to manipulate with positions for this


while True:

    user_guess = input("guess the word: ")
    clear()

#check if he has already guessed and show the letter
    if user_guess in display:
        print(f"You have already guessed {user_guess}")

#looping thrugh indexes
    for position in range(len(orignal_word)):
        if user_guess == orignal_word[position]:
            display[position] = user_guess
    print(display)

# to check if person has won
    if "_" not in display:
        print("You won sir")
        break


#reducing lives
    elif user_guess not in orignal_word:
        lives = lives-1
        print(f"You guessed it wrong sir. This letter {user_guess} is not in the Word.")
        print(stages[lives])
        if lives == 0:
            print("you loose, sorry!")
            break







