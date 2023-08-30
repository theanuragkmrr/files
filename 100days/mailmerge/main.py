# placeholder='[name]'
# with open("./Input/Names/invited_names.txt","r") as f:
#     names=f.readlines()
#
#
#
#
# with open("./Input/Letters/starting_letter.txt") as t:
#     letters=t.read()
#     for name in names:
#
#         new_letter=letters.replace(placeholder,name.strip())
#         with open(f"./Output/ReadyToSend/letter_send_to_{name.strip()}.txt","w") as l:
#             l.write(new_letter)


placeholder="[name]"
with open("./Input/Names/invited_names.txt") as names:
    n=names.readlines()

with open("./Input/Letters/starting_letter.txt") as letters:
    letter=letters.read()
    for name in n:
        nl=letter.replace(placeholder,name.strip())
        with open(f"./Output/sending_to_{name.strip()}.txt","w")as t:
            t.write(nl)
