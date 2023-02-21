import os
import customtkinter as ct
from ctk_entryframe import CTkEntryFrame
import ApplicationSorter
import pickle
import time

Waittime=6480000#Time Range that program will toggled off already marked companies by itself so that you could reapply
States='Lexicographically'
Name='Vuong Duong' #Change this for changing users name



PathList1=os.path.join(os.path.dirname(__file__), "List1.txt")#This path point to List1
PathLog1=os.path.join(os.path.dirname(__file__), "Logging.txt")#This path point to Log file
PathDiction1=os.path.join(os.path.dirname(__file__), "dictionstoring.txt")# This path point to dictionstoring





ct.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ct.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
dictoggle={};dicposition={};dictime={}#for the purpose of sorting and toggling logic
GroupedLi=[]

class wind(ct.CTk):
    
    def __init__(self):
        global dictoggle,dicposition,dictime,GroupedLi,States
        super().__init__()
        
        self.title("ITEApplication.py")
        self.geometry(f"{1100}x{580}")
        #self.resizable(False, False)
 
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure((0,1,2), weight=1)

        #firstframe
        self.SideFrame= ct.CTkFrame(self,width=150,corner_radius=0)
        self.SideFrame.grid(row=0,column=0,rowspan=3,sticky='nsew')
        self.SideFrame.grid_columnconfigure((0),weight=1)
        self.SideFrame.grid_rowconfigure(1,weight=1)

        
        self.logo_label = ct.CTkLabel(master=self.SideFrame, text=Name, font=ct.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.scrollable_frame = ct.CTkScrollableFrame(master=self.SideFrame, label_text="Application List")
        self.scrollable_frame.grid(row=1, column=0,rowspan=4,columnspan=4, padx=(0, 0), pady=(10, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        self.scrollable_frame_switches = []
        #scrollable list content
        with open(PathList1,'r') as f:
            self.Lines=f.read().splitlines()        
        for i,val in enumerate(self.Lines):
            switch = ct.CTkSwitch(master=self.scrollable_frame, text=val,command=lambda charac=val , index=i: self.changestate(charac,index))#lambda index=i: self.changestate(index)
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)


        #secondframe
        self.MainFrame= ct.CTkFrame(self,fg_color='transparent')
        self.MainFrame.grid(row=0,column=1,sticky='nsew')
        self.MainFrame.grid_rowconfigure((0,1,5,6,7), weight=1)
        self.MainFrame.grid_columnconfigure((0), weight=1)
        self.sortratio=ct.CTkOptionMenu(master=self.MainFrame, values=["Lexicographically","Not Yet Applied","Applied"],command=self.sortevent)
        self.sortratio.grid(row=0,column=0,pady=(20,0),sticky='n')
        self.typer= ct.CTkTextbox(master=self.MainFrame,corner_radius=10,height=350)
        self.typer.grid(row=1,column=0,rowspan=3,padx=(10,10),sticky='nsew')
        self.submit1=ct.CTkButton(master=self.MainFrame,text="Submit",corner_radius=10,command=self.trigger_testing)
        self.submit1.grid(row=5,column=0,pady=10,sticky='ns')
        self.DiagBox1 = ct.CTkButton(master=self.MainFrame, text="Delete Content",corner_radius=10, command=self.Delcontent)
        self.DiagBox1.place(relx=0.5, rely=0.5, anchor=ct.CENTER)
        self.DiagBox1.grid(row=6,column=0,pady=10,sticky='ns')
        self.Progress1=ct.CTkProgressBar(master=self.MainFrame)
        self.Progress1.grid(row=7,column=0,padx=10,pady=30,sticky='s')
        self.Progress1.configure(mode="indeterminnate") 
        self.Progress1.start()

        #thirdFrame
        self.SideFrame2 = ct.CTkFrame(self)
        self.SideFrame2.grid(row=0,column=2,sticky = 'nsew')
        self.SideFrame2.columnconfigure(0,weight=1)
        self.SideFrame2.rowconfigure((1),weight=1)
        self.colorchanger1=ct.CTkOptionMenu(master=self.SideFrame2, values=["Dark","Light"],command=self.changecolor)
        self.colorchanger1.grid(row=0,column=0,pady=20,sticky='nsew')
        self.SideBox1=ct.CTkTextbox(master=self.SideFrame2,text_color='gray')
        self.SideBox1.grid(row=1,column=0,padx=10,pady=(0.20),sticky='nsew')

        #log content
        with open(PathLog1,'r') as f:
            Lines2=f.readlines()
            curprint="".join(Lines2)
            self.SideBox1.insert("0.0",curprint)
            self.SideBox1.configure(state='disabled')

        #Retrieve Pickle dictionary data  for True and False state of Switch
        with open(PathDiction1, "rb") as f:#dictionary to keep track of true false state
            GroupedLi=pickle.load(f)
        times=time.time()
        dictoggle,dicposition,dictime=GroupedLi[0],GroupedLi[1],GroupedLi[2]
        self.scanli1=[i for i in dictoggle if dictoggle[i] == True]#get key in dic with specific value IE (if got toggle on: in this case 1)
        self.scanli2=[i for i in dictime if dictime[i] !=0 and times>dictime[i]]
        if len(self.scanli1) !=0:
            for i in self.scanli1:
                self.scrollable_frame_switches[dicposition[i]].select()
        if len(self.scanli2) !=0: 
            print(self.scanli2)
            for i in self.scanli2:
                #dictime[i]=0
                log=f'System: Toggled off value of {str(i)} since the amount of time {str(Waittime)} has been met\n\n'
                self.logging(log)
                self.scrollable_frame_switches[dicposition[i]].toggle()#deselect if specific time of daterange meet: in this case, set as 75 days from the time of checking   


    def trigger_testing(self):
        global dictoggle,dicposition,dictime
        if len(self.typer.get("1.0",'end-1c'))>0:
            temp=[part for part in self.typer.get("1.0",'end-1c').split('\n') if part != '']#list comprehension to extract list from provided data that are turned into string by CTk
            print(temp)
            with open(PathList1,'a') as f:
                for i in temp:
                    f.write(f'{i}\n')
                    dictoggle[i]=False;dictime[i]=0#modify dictime and dictoggle
            log=f'Added {temp} to the System\n\n'
            self.logging(log)
            self.typer.delete("1.0",'end')
            self.Lines, dicposition=ApplicationSorter.sortLexico()#ADD IN Dicposition
            Li=[dictoggle,dicposition,dictime]
            with open(PathDiction1, "wb") as k:
                print('accessed')
                pickle.dump(Li, k)
            self.sortevent(States)
            
        #self.logging()
    def sortevent(self,currentval):# Sorting
        global States
        States= currentval
        self.scanli1=[i for i in dictoggle if dictoggle[i] == True]
        if currentval == 'Lexicographically':
            temp=self.Lines
        elif currentval == 'Applied':    
            temp=self.scanli1
        else:
            temp=[i for i in self.Lines if i not in self.scanli1]
        self.scrollable_frame.destroy()
        self.scrollable_frame = ct.CTkScrollableFrame(master=self.SideFrame, label_text="Application List")
        self.scrollable_frame.grid(row=1, column=0,rowspan=4,columnspan=4, padx=(0, 0), pady=(10, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []   
        tempLi={}
        for i,val in enumerate(temp):   
            tempLi[val]= i
        for i,val in enumerate(temp):
            switch = ct.CTkSwitch(master=self.scrollable_frame, text=val,command=lambda charac=val , index=i: self.changestate(charac,index))#lambda index=i: self.changestate(index)
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)
        if len(self.scanli1) !=0 and currentval != 'Not Yet Applied':
            for i in self.scanli1:
                self.scrollable_frame_switches[tempLi[i]].select()


    def logging(self, logger):
        with open(PathLog1,'a') as f:#change from 'a' to 'w' if prefre one-time logfile, IE session log, meaning full log will not exist when program end
            self.SideBox1.configure(state='normal')
            f.writelines(logger)

            #self.SideBox1.delete("0.0","100.0")
            self.SideBox1.insert("0.0",logger)
            self.SideBox1.configure(state='disabled')

    def changecolor(self,setc : str): #Set Appearance Mode
        ct.set_appearance_mode(setc.lower())
    
    def Delcontent(self):#Content Delete Function
        global dictoggle,dicposition,dictime
        while True:
            dialog = CTkEntryFrame(text="Input Company Name:", title="Janitor")#CTkInputDialog(text="Input Company Name:", title="Janitor")
            temp=''
            temp=dialog.get_input()
            if temp != None:
                if temp != '' or temp != ' ':
                    if dicposition.get(temp,-1) !=-1:
                        dictime.pop(temp);dictoggle.pop(temp)
                        self.Lines,dicposition=ApplicationSorter.delvalue(temp)
                        log=f'Deleted all instances of "{temp}" from the System\n\n'
                        self.logging(log)
                        Li=[dictoggle,dicposition,dictime]
                        with open(PathDiction1, "wb") as k:
                            print('accessed')
                            pickle.dump(Li, k)
                        self.sortevent(States)
                else:
                    print('No value returned')
            else:
                print('value canceled')
                break

    
    def changestate(self,val,index):#toggle switch
        dictoggle[val]=not dictoggle[val]
        log=f'Switched value of {str(val)} to {str(dictoggle[val])}\n\n'
        self.logging(log)
        if dictoggle[val] == True:
            dictime[val]=time.time()+Waittime
        else:
            dictime[val]=0
        GroupedLi=[dictoggle,dicposition,dictime]
        with open(PathDiction1, "wb") as f:
            pickle.dump(GroupedLi, f)

    
if __name__ == "__main__":
    app = wind() 
    app.mainloop()
