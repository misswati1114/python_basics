Intro = input("Enter your intro: ")
count = 1
letters = 0
for i in Intro:
    letters = letters+1
    if(i==" "):
        count = count+1
print("No of letters are: ")
print(letters)
print("no of words are: ")
print(count)
