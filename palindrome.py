num=int(input("Enter the number:"))
n=num
num=str(num)
rev=num[::-1]
revn=int (rev)
if num==revn:
    print("number is  palindrome")
else:
    print("number is not  palindrome")
