a = int(input())
stepen = 0
while pow(2, stepen) <= a:
    stepen += 1
print(stepen)

if a == 1:
    stepen = 0
    print(stepen)
elif pow(a, 0.5)%2 == 0:
    while pow(2, stepen) < a:
        stepen +=1
    print(stepen)
else:
    print("НЕТ")



