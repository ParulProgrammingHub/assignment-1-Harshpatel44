def simple_interest(p,t,r):
    i=float(p*(1+(r*t)))
    print("Simple Interest is %s"%(i))
p_amount=float(input("Enter Principal Amount:"))
time=int(input("Enter Time:"))
rate=float(input("Enter Rate:"))
simple_interest(p_amount,time,rate)
