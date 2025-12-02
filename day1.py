f=open("input.txt","r")
d=f.read()
n=d.split('\n')
r=50
pas=0
#for first question move the checking conditions to previous indentation
for i in n:
    i = i.strip()
    if i[0]=="L":
        for j in range(int(i[1:])):
            r-=1
            if r<0:
                r+=100
            if r==0:
                pas+=1  
    elif i[0]=="R":
        for j in range(int(i[1:])):
            r+=1
            if r>=100:
                r-=100  
            if r==0:    
                pas+=1
print(pas)
print(r)
