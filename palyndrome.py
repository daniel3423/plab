def is_palindrome(s):
if s == s[::-1]:
return True
else:
return False

palin = []

for i in range(100,1000):
for j in range(100,1000):
tmp = i*j
neww = str(tmp)
if (is_palindrome(neww)):
palin.append(tmp)

print("the max is:",max(palin))




