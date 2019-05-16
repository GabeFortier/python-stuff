f = open('drinkList.txt', 'r')
firstt = [line for line in f.readlines()]

results = []
for x in firstt:
    results.append('<string name="%s">%s</string>\n'%(x.rstrip().replace(' ',''),x.rstrip()))

with open('newList.txt', 'w') as f:
    for item in results:
        f.write("%s" % item)