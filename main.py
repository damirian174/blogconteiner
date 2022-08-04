a = input()
list1 = ['I','V','x','L','C','D','M']
listL = {'I':1,'V':5,'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
l = list(a)
l1 = []

for i in l:

    x = listL[i]
    l1.append(x)

print(sum(l1))

#if a in listL:
#    print('Верно')

#    print(listL[a])
#else:
#    print('Неверно')
