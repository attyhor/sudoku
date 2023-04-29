numberoflines = 0
sudokutable = []
defaultset ={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

with open("feladat.txt", "r") as source:
    for line in source:
        numberoflines += 1
        new_string = ''.join(line.split('\n'))
        #print(new_string, len(new_string))
        #check valid
        if len(new_string) != 9:
            print("Error in txt file. Correct matrix is 9x9!")
            break
        """ numbersinline = [int(s) for s in new_string.split() if s.isdigit()] """
        sudokutable.append(new_string)


if numberoflines != 9:
    print("Error in txt file. Correct matrix is 9x9!")
    

#print(sudokutable)
print(sudokutable[2][1])
#check in line
""" for x in range(9):
    for y in range(9):
        print(sudokutable[x][y]) """