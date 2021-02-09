#odd even

num = 15
if(num%2==0):
    print("number is even")
else:
    print("number is odd")


## add numbers
def add_num(a,b):
    sum=a+b;
    return sum; 
num1=int(input("input the number one: "))
num2=int(input("input the number one :"))
print("The sum is",add_num(num1,num2))