def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print("Select Operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter your choice:(1,2,3,4)\n")

    if choice in('1','2','3','4'):
        num1 = float(input("Enter First number: "))
        num2 = float(input("Enter Secod number: "))

        if choice =='1':
            print(num1," + ",num2, " = ", add(num1,num2))
        elif choice =='2':
            print(num1," - ",num2, " = ", sub(num1,num2))
        elif choice =='3':
            print(num1," * ",num2, " = ", mul(num1,num2))
        elif choice =='4':
            print(num1," / ",num2, " = ", div(num1,num2))
        break
    else:
        print("Invalid Input!")
