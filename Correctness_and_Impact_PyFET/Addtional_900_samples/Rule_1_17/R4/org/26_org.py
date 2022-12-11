for i in dif_letters:
    count_letters[i] = word.count(i)

# Set tries to 0
tries = 0

# Main loop
while True:
    # Check if the user has used all of their tries
    if tries == 6:
        print(f"You did not guess the word!\nThe word was {word}")
        # Check if user wants to exit the program
        if user_inp == "q":
            break
# Get user input and make it all lower case
user_inp = input(">>").lower()