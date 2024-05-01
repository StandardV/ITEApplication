import pickle
import time
import os
Li=[]
dictoggle={}
dicposition={}
dictime={}

current_dir = os.path.dirname(os.path.abspath(__file__))

list1 = os.path.join(current_dir,"List1.txt")
diction_storing = os.path.join(current_dir,"dictionstoring.txt")




with open(list1,'r') as f:
    Lines=f.read().splitlines()        
for i,val in enumerate(Lines):
    dictoggle[val]=False# IMPLEMENT THIS INTO THE FUNCTION AS WELL, FOR BEST USE PUT THE LIST IN HERE AS WELL
    dictime[val]=0
    dicposition[val]=i

Li=[dictoggle,dicposition,dictime]

with open(diction_storing, "wb") as k:
    print('accessed')
    pickle.dump(Li, k)

GroupedLi=[];scanli=[]

with open(diction_storing, "rb") as k:#dictionary to keep track of true false state
    GroupedLi=pickle.load(k)
print(len(GroupedLi))
dictoggle,dicposition,dictime=GroupedLi[0],GroupedLi[1],GroupedLi[2]
scanli=[i for i in dictoggle if dictoggle[i] == True]
print(Lines)

