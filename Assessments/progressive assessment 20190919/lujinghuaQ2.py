infile = open('qbdata.txt','r')
outfile = open('lujinghua2.txt','w')
name = input("Please input a name: ")#full name
line = infile.readline()

index = 10001

while line:
    for i in range(len(line)):
        if line[i]==' ':
            '''
            #if input the first name
            if line[:i]!=name:
                line = str(index)[1:]+' '+line
                outfile.write(line)
                index +=1
            #if input the full name
            '''
            for j in range(i+1,len(line)):
                if line[j]==' ':
                    print(line[:j])
                    if line[:j]!=name:
                        outfile.write(line)
                    break
            break
    line = infile.readline()
infile.close()
outfile.close()
