sum=0
a=[]
for i in range(0,5):
    x=int(input("Enter Marks[%s]"%(int(i))))
    a.append(x)
    sum=int(sum)+x
mean=sum/5
if(mean<35):
    print("Fail with Percentage %s"%(mean))
else:
    print("Pass with Percentage %s"%(mean))