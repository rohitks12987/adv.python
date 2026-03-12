f = open("data.txt","r")
lines = f.readlines()
f.close()

if len(lines) > 1:
    del lines[1]

f = open("data.txt","w")
f.writelines(lines)
f.close()
print("Second line deleted successfully")