import os
x=os.path.join(os.path.dirname(__file__), "List1.txt")#This path point to List1
dicposition={}

def sortLexico():#just to check if current list==sorted --> that's it()but remember when submit value: need to write those value to the end first
    with open(x,'r') as f:
        Lines=f.read().splitlines()     
    Lines=sorted(Lines)
    for i,val in enumerate(Lines):
        dicposition[val]=i
    with open(x,'w')as f:
        for i in Lines:
            f.write(f"{i}\n")
    return Lines,dicposition
with open(x,'r') as f:
    Lines=f.read().splitlines()        
for i,val in enumerate(Lines):
    dicposition[val]=i

def delvalue(content):#This function responsible for delete and alter List and dicposition
    Li=[]
    with open(x, "r") as f:
        Lines=f.read().splitlines()   
    with open(x, "w") as f:
        for i,line in enumerate(Lines):
            if line != content:
                f.write(f'{line}\n')
                Li.append(line);dicposition[line]=i
        return Li, dicposition


