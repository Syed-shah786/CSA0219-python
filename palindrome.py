string=input("enter the string:")
alpha,digits,space,special=0,0,0,0
a=[]
d=[]
s=[]
spl=[]
for i in range(len(string)):
   if(string[i].isalpha()):
      alpha+=1
      a.append(string[i])
   elif(string[i].isdigit()):
         digit+=1
         d.append(string())
   elif(string[i].isspace()):
            space+=1
   else:
      special+=1
      spl.append(string[i])
print("vowels:",alpha,a)
print("digits:",digits,d)
print("space:",space,s)
print("special:",special,spl)
