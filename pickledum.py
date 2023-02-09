import pickle
import time
Li=[]
dictoggle={}
dicposition={}
dictime={}
with open(r"D:\Largecodefile\TkinterApply\List1.txt",'r') as f:
    Lines=f.read().splitlines()        
for i,val in enumerate(Lines):
    dictoggle[val]=False
    dictime[val]=0
    dicposition[val]=i



Li=[dictoggle,dicposition,dictime]

with open(r"D:\Largecodefile\TkinterApply\dictionstoring.txt", "wb") as k:
    print('accessed')
    pickle.dump(Li, k)

GroupedLi=[];scanli=[]

with open(r"D:\Largecodefile\TkinterApply\dictionstoring.txt", "rb") as k:#dictionary to keep track of true false state
    GroupedLi=pickle.load(k)
print(len(GroupedLi))
dictoggle,dicposition,dictime=GroupedLi[0],GroupedLi[1],GroupedLi[2]
scanli=[i for i in dictoggle if dictoggle[i] == True]
print(scanli)
