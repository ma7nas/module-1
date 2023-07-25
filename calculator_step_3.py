operations = ('x', '+', '-', '/', '^')
symbol=''

with open("step_3.txt", 'r') as calcs:
    calculations = calcs.read().splitlines()

line_number = 1
lines_visited = []

while True:
    file_string = calculations[line_number-1]
    print(file_string)
    string_list = file_string.split(" ")
    print(string_list)
    if string_list[1] == "calc":
        symbol = string_list[2] 
        a = string_list[3] 
        b = string_list[4] 
        if symbol == 'x':
            symbol = '*'
        if symbol == '^':
            symbol = '**'
        calc = a + ' ' + symbol + ' ' + b
        try:
            line_number = int(eval(calc))
        except ZeroDivisionError:
            line_number = 0
    else:
        line_number = int(string_list[1])
    if line_number not in lines_visited:
        lines_visited.append(line_number)
        continue
    else:
        print("Breaking at line " + str(line_number) + "\nStatement is " + '"' + calculations[line_number-1] + '"')
        break











    
