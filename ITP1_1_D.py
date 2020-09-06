s = int(input())

hour = s // 3600
s = s - hour*3600
minutes = s // 60
s = s - minutes*60

print(str(hour) + ":" + str(minutes) + ":" + str(s))
