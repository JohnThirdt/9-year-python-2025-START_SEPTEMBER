word = input()


a = {}
for i in word:
   if i in a:
        a[i] += 1
   else:
       a[i] = 1

print(list(a.values()).sort())