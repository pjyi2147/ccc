#### 2010 j3 
string = input().split()
order = string[0]

dic = {}

while order in '123456':
    x = string[1]
    if order == '1':
        dic[x] = int(string[2])

    elif order == '2':
        print(dic[x])

    elif order == '3':
        y = string[2]
        value_x = int(dic[x])
        value_y = int(dic[y])
        value_x = value_x + value_y
        dic[x] = value_x

    elif order == '4':
        y = string[2]
        value_x = int(dic[x])
        value_y = int(dic[y])
        value_x = value_x * value_y
        dic[x] = value_x

    elif order == '5':
        y = string[2]
        value_x = int(dic[x])
        value_y = int(dic[y])
        value_x = value_x * value_y
        dic[x] = value_x

    elif order == '6':
        y = string[2]
        value_x = int(dic[x])
        value_y = int(dic[y])
        value_x = value_x - value_y
        dic[x] = value_x 

    string = input().split()
    order = string[0]


