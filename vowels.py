string=input("enter the string:")
vow="AaEeIiOoUu"
v=0
c=0
vowels=[]
cons=[]
for i in range(len(string)):
   if string[i] in vow:
    v+=1
    vowels.append(string[i])
   else:
        c+=1
        cons.append(string[i])
print("\n vowels:",vowels,v)
print("\n cons:",cons,c)

