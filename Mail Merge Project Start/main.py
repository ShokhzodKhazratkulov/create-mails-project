
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

for i in names:
    stripped_i = i.strip()
    ready_letters = letter.replace("[Name]", stripped_i)
    with open(f"./Output/ReadyToSend/letter for {stripped_i}.txt", mode="w") as completed_letters:
        completed_letters.write(ready_letters)
    




