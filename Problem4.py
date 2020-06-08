no = int(input())
a = []
for it in range(no):
    a.append(int(input()))

j = 0

for i in range(no):
    f= 0
    
    while(i >= 0):
        i = a[i]-1
        f =f+ 1
    j = max(f, j)
    
print(j)