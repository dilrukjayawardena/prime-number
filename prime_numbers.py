
num=6


#using maps
data=list(map(lambda x: num%x==0,range(2,num)))
if True in data:
  print("not a prime number")
else:
  print("prime number")

#using filters
data=list(filter(lambda x: num%x==0,range(2,num)))
if len(data)>0:
  print("not a prime number")
else:
  print("prime number")