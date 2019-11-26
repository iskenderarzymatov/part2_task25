x = input("Enter to here: ").split()
s = "1"
for i in x:
    if len(i) > len(s):
        s = i
print(s)