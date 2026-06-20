n = int(input('How many elements? '))
my_list = []

for i in range(n): 
    element = input('Element ' + str(i + 1) + ' is: ')
    my_list.append(element)

print('Your List is: ', my_list)

def listToString(my_list): 

    stringed = ''

    if len(my_list) > 2: #list has more than 2 elements

        for j in range(len(my_list)):
            stringed += (my_list[j])
            if j != (len(my_list) - 1):
                stringed += ', '
            if j == (len(my_list) - 2): 
                stringed += 'and '
        
    elif len(my_list) == 2: #List has only 2 elements
        for k in range(2): 
            stringed += (my_list[k])
            if k == 0: 
                stringed += ' and '
    elif len(my_list) == 1: #has only 1
        stringed += my_list[0]

    return stringed      
   
print('String from List is: ' + listToString(my_list))