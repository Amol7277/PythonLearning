print("PASS KEYWORD")
for i in range(0, 5):
    if i == 3:
        pass
    print("Number :", i)

for j in range(5):
    if j == 3:
        pass
    print("Number: ", j)

print("CONTINUE KEYWORD")
for k in range(5):
    if k == 3:
        continue
    print("Number :", k)

print("BREAK KEYWORD")
for l in range(5):
    if l == 3:
        break
    print("Number :", l)