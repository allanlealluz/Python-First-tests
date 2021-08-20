part1 = [ [ ],[ ],[ ] ]
part2 = [ [ ],[ ],[ ] ]
part3 = [ [ ],[ ],[ ] ]
c = 0
while c < 9:
    n = int(input('digite um numero: '))
    if(c <= 2):
        part1[c].append(n)
    elif(c > 2 and c <= 5):
        part2[c-4].append(n)
    else:
        part3[c-6].append(n)
    c+=1
print(part1)
print(part2)
print(part3)