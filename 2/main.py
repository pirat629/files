f = open("17 (2).txt")
s = [int(i) for i in f]
maxi = 0
ind = 0
for i in range(7, len(s), 7):
    if sum(s[i-7:i]) > maxi:
        maxi = sum(s[i-7:i])
        ind = i
x = s[ind-7:ind]
dweek = x.index(max(x))+1
week = ind//7
print(dweek, week)