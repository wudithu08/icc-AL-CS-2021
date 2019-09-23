FileWrite = open('HealthCare.txt','w')

end = '' #string

while end != '!':
    name = input('Input name:') #string
    height = input('Input height:') #string
    weight = input('Input weight:') #string
    VitalCapacity = input('Input vital capacity:') #string
    WriteInformation = name + ' ' + height + ' ' + weight + ' ' + VitalCapacity + '\n' #string
    FileWrite.write(WriteInformation)
    end = input('If you want to stop inputting information,please input"!":')

FileWrite.close()
    
