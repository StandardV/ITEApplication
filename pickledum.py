import pickle
import time
import os
Li=[]
dictoggle={}
dicposition={}
dictime={}
with open(os.path.join(os.path.dirname(__file__), "List1.txt"),'r') as f:
    Lines=f.read().splitlines()        
for i,val in enumerate(Lines):
    dictoggle[val]=False
    dictime[val]=0
    dicposition[val]=i

Li=[dictoggle,dicposition,dictime]

with open(r"D:\Largecodefile\TkinterApply\dictionstoring.txt", "wb") as k:#Store Dictionaries data, this process should only happen once when set up
    print('accessed')
    pickle.dump(Li, k)

#GroupedLi=[];scanli=[]
#with open(r"D:\Largecodefile\TkinterApply\dictionstoring.txt", "rb") as k:#dictionary to keep track of true false state
#    GroupedLi=pickle.load(k)
#print(len(GroupedLi))
#dictoggle,dicposition,dictime=GroupedLi[0],GroupedLi[1],GroupedLi[2]
#scanli=[i for i in dictoggle if dictoggle[i] == True]

#Able to use the above line to load back the file and check for stored data


