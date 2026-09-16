starinput = int(input())
text = ""
space = " "
for i in range(starinput):
    text = ""
    for x in range(i+1):
      text += "*"
      text += space
      for y in range(starinput - x):
        spaces = space * y
    print(spaces + text)