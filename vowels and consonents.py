st=input("Enter a string: ")
v,c=0,0
vo='aeiouAEIOU'
for i in st:
    if i in vo:
        v+=1
    elif i==" ":
        continue
    else:
        c+=1
print("Number of vowels:",v,"\nNumber of consonents:",c)
