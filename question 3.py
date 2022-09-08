num = int(input("Enter number"))

def filter(num):
    even =[]   
    for i in range(num):
        if(i%2==0) and (i !=0):
            even.append(i)
            
    print(f"Even list is :{even}")


filter(num)

