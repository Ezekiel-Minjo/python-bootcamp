fileptr = open("file.txt", "r")

if fileptr:
  print("file is opened successfully")
content = fileptr.read(10)
content = fileptr.readline()
content = fileptr.readline()
print(type(content))
print(content)
fileptr.close()
