p= float (input ("enter the principal amount:"))
r= float (input("enter the rate of intrest:"))
t= float (input("enter the time in year:"))
x=(1+r/100)**t
CI=p*x-p
print("compound intrest is:",round(CI,2))
