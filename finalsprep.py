x = "shit i got to hypenate"
y = ""
for c in x:
    y = y+c+"-"
print(y)


tot = 100
for ctr in range(100,1,-1):
    if ctr % tot ==0:
        print(ctr)
    

mylist = ['bob', 'jim', 'fred']
for name in mylist:
  if name == 'jim':
   mylist.remove('jim')
   mylist.append('Jimbo')
  else:
   print(name)
  
