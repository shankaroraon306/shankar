num=int(input("enter the number:"))
for i in range(2,num):
    if num % i==0:
        print(num,"is not a prime number")
        break
    else:
        print(num,"is a prime number")
        break
