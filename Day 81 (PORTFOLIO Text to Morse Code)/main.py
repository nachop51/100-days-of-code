from data import morse_values

user_input = input("Enter some text: ").lower().strip()

for letter in user_input:
    if letter in morse_values:
        print(morse_values[letter], end=" ")
    else:
        print(f"Invalid input, character {letter} not valid")
        break
