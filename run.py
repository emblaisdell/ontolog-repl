
SPACING = 5

while True:
    line = input(" "*SPACING)
    if line=="exit":
        break
    elif line=="in":
        SPACING+=1
    elif line=="out":
        SPACING-=1
    else:
        print(line)
