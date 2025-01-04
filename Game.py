import random
from Words import animals, countries, fruits
from Stickman import hangman_stage


def play():
    print("Welcome To Hangman!\n")

    categories = {
        "1": ("Animals", animals),
        "2": ("Countries", countries),
        "3": ("Fruits", fruits)
    }

    print("Choose A Category:")
    for key, (name, _) in categories.items():
        print(f"{key}: {name}")
    
    while True:
        choice = input("\nEnter Your Choice: ").strip()

        if choice in categories:
            break
        else:
            print("Invalid Choice! Please Try Again!")

    category_name, words = categories[choice]
    word = random.choice(words).lower()
    guessed_letters = []
    attempts = 6

    print(f"You've Chosen {category_name}! Let's Begin!")

    while attempts > 0:
        current_word = ""
        for letter in word:
            if letter in guessed_letters or letter == " ":
                current_word += letter
            else:
                current_word += "_"
    
        if "_" not in current_word:
            print(f"\nCongrats! You've Guessed The Word: {word}")
            break

        print(hangman_stage(attempts))
        print(f"Word: {current_word}")
        print(f"Guessed Letters: {" ".join(sorted(guessed_letters))}")

        guess = input("\nGuess A Letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Choice! Please Guess A Single Letter!")
            continue

        if guess in guessed_letters:
            print("You've Already Guessed That Letter!")
            continue

        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Well Done! {guess} Is In The Word!")
        else:
            print(f"Oof! {guess} Is Not In the Word!")
            attempts -= 1

    
    if attempts == 0:
        print(hangman_stage(attempts))
        print(f"\nYou Lost! You Haven't Guessed The Word: {word}")
    

def main():
    while True:
        play()
        again = input("\nPlay Again? (yes(y)/no(n)): ").strip().lower()
        if again != "yes" and again != "y":
            break


if __name__ == "__main__":
    main()