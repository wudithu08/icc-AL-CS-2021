FileWrite = open('HealthCare.txt','w')

end = '' #STRING

while end != '!':
    name = input('Input name:') #STRING
    height = input('Input height:') #STRING
    weight = input('Input weight:') #STRING
    VitalCapacity = input('Input vital capacity:') #STRING
    WriteInformation = name + ' ' + height + ' ' + weight + ' ' + VitalCapacity + '\n' #STRING
    FileWrite.write(WriteInformation)
    end = input('If you want to stop inputting information,please input"!":')#STRING

FileWrite.close()
