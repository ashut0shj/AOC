def checker(c,r,g,b):
    flag = True
    if c['red'] > r and c['green'] > g and c['blue'] > b:
        return True
    else: 
        return False



r = 12
g = 13
b = 14
keys =[]
lines = []
with open('2023\day2.txt','r+') as file:
    for i in file:
        lines.append(i.rstrip('\n').lstrip('Game '))
sum  = 0
for i in lines:
    i = i.split(': ')
    key = int(i[0])
    value = i[1].split(';')
    #print(value)
    flag = True
    for part in value :
        count = {'red' : 0 , 'green' : 0, 'blue' : 0}
        part  = part.strip().split(', ')
        for game in part:
            num, color = game.split()
            num = int(num)
            if num > count[color]:
                count[color] = num
        print()
        print(count, end = '   ...   ')
        if count['red'] > r or count['green'] > g or count['blue'] > b:
            flag = False
            print(count,9999999999)
            break
    if flag == True:
        keys.append(key)
        sum = sum + key
print(keys, sum)

