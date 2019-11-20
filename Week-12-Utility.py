#https://github.com/vmessmore/Week-12-Assignment-A
#Tori Messmore
#CSCI-Section C
#Week 12-Part B

def PrintOutput(the_string):
    print('OUTPUT', the_string)

def LoadFile(file_name):
    lines = []
    file = open(file_name, 'r', encoding='utf-8-sig')
    file_lines = file.read().splitlines()
    return file_lines

def UpdateString(original, edit, number):
    new_string=''
    for i in range(len(original)):
        if i == number:
            new_string += edit
        else:
            new_string += original[i]
    PrintOutput(new_string)

def FindWordCount(input_list, input_string):
    num_times = input_list.count(input_string)
    return num_times

def ScoreFinder(name_list, score_list, person):
    boo=False
    for i in range(len(name_list)):
        this_name = name_list[i]
        if this_name.lower() == person.lower():
            boo=True
            output = str(name_list[i]) + ' got a score of ' + str(score_list[i])
            PrintOutput(output)
    if boo==False:
        PrintOutput('player not found')

def Union(list_1, list_2):
    new_list=[]
    for i in range(len(list_1)):
        if list_1[i] in new_list:
            pass
        else:
            new_list.append(list_1[i])
    for i in range(len(list_2)):
        if list_2[i] in new_list:
            pass
        else:
            new_list.append(list_2[i])
    return new_list
        
def Intersection(list_1, list_2):
    new_list=[]
    for i in range(len(list_1)):
        if list_1[i] in list_2:
            new_list.append(list_1[i])
    return new_list

def NotIn(list_1, list_2):
    new_list=[]
    for i in range(len(list_1)):
        if list_1[i] not in list_2:
            new_list.append(list_1[i])
    return new_list
