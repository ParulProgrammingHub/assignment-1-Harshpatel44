days=input("Enter the days:")
years=int(int(days)/365)
months=int((int(days)%360)/30)
ds=(((int(days)%360)%30))
print("Years: %s ,Months: %s ,Days: %s"%(years,months,ds))

