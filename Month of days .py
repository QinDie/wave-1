one = ["Jan", "Mar", "May" ,"Jul" ,"Aug", "Oct","Dec"] 
two  = ["Apr","Jun","Sep","Nov"]

if str(input())in one :
    print("31 days")
    
elif str(input()) in two :
    print("30 days")
    
else : 
    print("28 or 29 days")
