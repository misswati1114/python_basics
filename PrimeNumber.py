number = int(input("Enter the number: "))
count = 0
for num in range(1,number):
    if (number%num==0):
        count=count+1
if(count==2):
    print("Number is Prime")
else:
    print("Number is non-prime")
