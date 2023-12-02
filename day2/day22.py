r = 12
g = 13
b = 14
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
    count = {'red' : 0 , 'green' : 0, 'blue' : 0}
    for part in value :
        part  = part.strip().split(', ')
        for game in part:
            num, color = game.split()
            num = int(num)
            if num > count[color]:
                count[color] = num
    power = count['red'] * count['green'] * count['blue']
    sum += power
    print(count, power)
print((sum))

