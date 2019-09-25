infile=open("qbdata.txt",'r')
outfile=open("LujinghuaQ1.txt",'w')
newchar = input("Please input the replace character")
line = infile.readline()
while line:
    newline = ''
    '''
    for i in line:
        if i !=' ':
            newline+= i
        else:
            newline+= newchar
    '''
    for i in range(len(line)):
    	if line[i]!=' ':
    		newline += line[i]
    	else:
    		newline += newchar

    outfile.write(newline)
    line = infile.readline()
infile.close()
outfile.close()




