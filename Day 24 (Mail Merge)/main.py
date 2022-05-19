with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()
file.close()

names = list(map(lambda x: x.strip('\n'), names))

with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()
file.close()

for name in names:
    name = name.strip(' ')
    with open(f"Output/ReadyToSend/letter_for_{name[:]}.txt", "w") as file:
        file.write(letter.replace("[name]", name))
    file.close()
