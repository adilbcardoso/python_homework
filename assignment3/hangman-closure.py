def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter.lower())

        letter_guessed = ""

        for char in secret_word:
            if char.lower() in guesses:
                letter_guessed += char
            else: 
                letter_guessed += "_"

        print (letter_guessed)

        return "_" not in letter_guessed
    
    return hangman_closure

#hangman execution


secret_word = input("Enter the secret word:").strip()

hangman = make_hangman (secret_word)

print ("\nStart guessing letters!")

while True:

    guess = input("Guess a letter:").strip()
    

    if not guess:
        print("Please enter a letter")
        continue

    finished = hangman(guess)

    if finished:
        print("congratulations! You have guessed the word!")
        break








