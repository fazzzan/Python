cell1 = input()
cell2 = input()
aceg = ['a', 'c', 'e', 'g' ]
bdfh = ['b', 'd', 'f', 'h' ]
if cell1.lower() == cell2.lower():
    print("YES")
if ((cell1[0].lower() in aceg) and (cell2[0].lower() in aceg)) or ((cell1[0].lower() in bdfh) and (cell2[0].lower() in bdfh)):
    if int(cell1[1])%2 == int(cell2[1])%2:
        print("YES")
    else:
        print("NO")
else:
    if int(cell1[1])%2 != int(cell2[1])%2:
        print("YES")
    else:
        print("NO")

