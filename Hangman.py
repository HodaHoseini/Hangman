import words, random
chosen_word = random.choice(words.word_list)

guessed_words = ""

blanks = []
for letter in chosen_word:
    blanks.append("_")
mistake = ""
lives = 6
end = False
while not end:

        guess = input("Guess a letter: ").lower()
        if guess in guessed_words:
            print("You already guessed this letter.")
        guessed_words += guess
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                blanks[index] = guess


        if guess not in chosen_word:

            lives -= 1
            mistake += '''/'''
            print(f"You have {lives} lives left.")
            print(f"Your mistake: {mistake}")


        print(blanks)
        if "_" not in blanks:
            end = True
            print("You won!")
        if lives == 0:
            end = True
            print("You lost!")



