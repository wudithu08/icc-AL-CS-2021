infile = open('lujinghua2.txt','r')
number = input("Please input a number: ")
line = infile.readline()
'''
while line:
    if number in line:
        print(line)
        break
    line = infile.readline()
else:
    print("Sorry, the item you are searching is not exist")
    
'''
match = False
while line:
    for i in range(len(line)):
        if line[i] == ' ':
            if line[:i]== number:
                print(line)
                match = True
                break
    line = infile.readline()
if match == False:
    print("Sorry, the item you are searching is not exist")

infile.close()

