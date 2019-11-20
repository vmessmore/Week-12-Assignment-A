def PrintOutput(the_string):
    print('OUTPUT', the_string)

def LoadFile(file_name):
    lines = []
    file = open(file_name, 'r', encoding='utf-8-sig')
    file_lines = file.read().splitlines()
    return file_lines
