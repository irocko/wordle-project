import random

#welcome and instructions
def welcome_screen():
    print("Welcome to Wordle!")
    print("How to play:")
    print("- I'll think of a 5-letter word and you will have 6 guesses")
    print("- I have a bank of 12972 words that are valid")
    print("- If a letter is correct, it will show green")
    print("- If a letter is wrong, it will show grey")
    print("- A correct letter, but in the wrong place shows yellow")
    print("Have fun!")
    return
welcome_screen()

#read files and appending words to a list   
target_list = []
valid_list = [] 
with open("target_words.txt") as target_words:
    for words in target_words:
        target_list.append(words.strip())
with open("all_words.txt") as valid_words:
    for words in valid_words:
        valid_list.append(words.strip())

#selecting a random target word 
target_word = random.choice(target_list)

#for test cases: initialize below your specific target_word = "wordhere",  and put # above
#target_word = "put whatever word you want here"

#for testing purposes, can print target word if needed
print(target_word)

#clue identifiers
green_clue = '🟩 '
yellow_clue = '🟨 '
grey_clue = '⬜ '

#start of guess loop    
attempts = 1
while attempts <= 6:
    guess = input("\nAttempt #{}: ".format((attempts)))
    guess = guess.lower()
#what to do if guess is correct
    if guess == target_word:
        print(green_clue*5)
        for letter in target_word:
            print(" "+ letter.upper(), end=' ')
        print(f"\n\nYOU GOT IT!\nNUMBER OF GUESSES: {attempts}")
        break
#scoring algorithm if guess is not correct. Starts with a check if guess is valid.
    else:
        if guess in valid_list:
            attempts += 1
            for letter in guess:
                if letter in target_word and guess.index(letter) == target_word.index(letter):
                    print(green_clue,end='')
                elif letter in target_word and guess.index(letter) != target_word.index(letter):
                    print(yellow_clue,end='')
                else:
                    print(grey_clue,end='')
            print()
            for letter in guess:
                print(" "+ letter.upper(), end=' ')
        else:
#what to do if word is not valid.
            print("Word is not valid. Don't worry, I won't count it as an attempt. Try again :)")
            continue
#what to do if all 6 attempts are done without correct guess.
        if attempts > 6:
            print(f"\nYou lost! the word I was thinking of was {target_word.upper()}!")


#note to self:

#scoring is a bit tricky with words with doubles letters.e.g target word = river, but rivet makes all green boxes
#work on this next. 
#possible ideas: 
#while iterating through the letters of guessword, place relevant clue, then add letter to list, and implement a check that if it comes across again, place green/yellow clue
#completely redo the loop but instead of for loop use: for range(len()) and guess[i] = target[i]

#ask senior for opinions on welcome screen/instructions
#review pseudo code,flowchart with senior