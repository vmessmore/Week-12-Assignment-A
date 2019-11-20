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
