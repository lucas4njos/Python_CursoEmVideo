#Python exercise 106: Make a mini-system that utilizes Python Interactive Help.
# The user is going to type the command and the manual will show up.
# When the user types the word 'FIM' ('END'), the program will close. Important: Use colors.

while True:

    varHelp = str(input('\033[1;37;40mQual função deseja conferir? \033[m')).strip()
    if varHelp == 'END':
        break
    else:
        print('\033[1;34;40m')
        help(varHelp)
        print('\033[m')