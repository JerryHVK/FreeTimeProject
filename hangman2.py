import random
import os

# would be a large dictionary
wordDictionary = ["sunflower", "house", "diamond", "memes", "yeet", "hello", "howdy"]

# print a hangman depend on how many mistake the player makes
def print_hangman(wrong):
    if(wrong == 0):
        print(" ------")
        print(" |    |")    
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("     _|_")
    elif(wrong == 1):
        print(" ------")
        print(" |    |")    
        print(" O    |")
        print("      |")
        print("      |")
        print("      |")
        print("     _|_")
    elif(wrong == 2):
        print(" ------")
        print(" |    |")    
        print(" O    |")
        print(" |    |")
        print("      |")
        print("      |")
        print("     _|_")

    elif(wrong == 3):
        print(" ------")
        print(" |    |")    
        print(" O    |")
        print("/|    |")
        print("      |")
        print("      |")
        print("     _|_")

    elif(wrong == 4):
        print(" ------")
        print(" |    |")    
        print(" O    |")
        print("/|\\   |")
        print("      |")
        print("      |")
        print("     _|_")

    elif(wrong == 5):
        print(" ------")
        print(" |    |")    
        print(" O    |")
        print("/|\\   |")
        print("/     |")
        print("      |")
        print("     _|_")
        
    elif(wrong == 6):
        print(" ------")
        print(" |    |")    
        print(" O    |")
        print("/|\\   |")
        print("/ \\   |")
        print("      |")
        print("     _|_")


def input_letter():
    print("Input a letter:", end = " ")
    c = input()[0]
    return c.lower()


def check_letter(randomWord: str,
                 wordArea: str,
                 wrong: int,
                 letter: chr):
    if letter in randomWord:
        letter_list_1 = [i for i in randomWord]
        # print(letter_list_1)
        letter_list_2 = [i for i in wordArea]
        # print(letter_list_2)
        for i in range(len(letter_list_1)):
            if letter_list_1[i] == letter:
                letter_list_2[i] = letter
        wordArea = ""
        for i in letter_list_2:
            wordArea += str(i)
    else:
        wrong += 1
    
    return wordArea, wrong

def raise_result(num_of_letter: int,
                 letter: chr):
    if num_of_letter == 0:
        print(f"There is no '{letter}' in the word")
    elif num_of_letter == 1:
        print(f"There is 1 '{letter}' in the word")
    else:
        print(f"There are {num_of_letter} '{letter}' in the word")

def game_finish(wrong: int,
                word_area: str):
    if wrong == 6:
        print("YOU LOSE")
        return True
    elif '_' not in word_area:
        print("YOU WIN")
        return True
    else:
        return False

def start():
    wrong = 0
    randomWord = random.choice(wordDictionary)
    word_area = ""
    for i in randomWord:
        word_area += "_"
    
    letter = ''
    while True:
        os.system('cls')
        if(i != 0):
            word_area, wrong = check_letter(randomWord=randomWord, wordArea=word_area, wrong=wrong, letter=letter)
        print("Welcome to hangman")
        print("-------------------")
        print_hangman(wrong = wrong)
        print("")
        print("-------------------")
        print("")
        print(f"THE HIDDEN STRING: {word_area}")
        print("")
        print("-------------------")
        if(game_finish(word_area=word_area, wrong=wrong)):
            break
        letter = input_letter()


start()


        







