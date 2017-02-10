import math
def comp_interest(p,t,r):
    i=float(p*(math.pow(1+r,t)))
    print("Compound Interest is %s"%(i))
p_amount=float(input("Enter Principal Amount:"))
time=int(input("Enter Time:"))
rate=float(input("Enter Rate:"))
comp_interest(p_amount,time,rate)
