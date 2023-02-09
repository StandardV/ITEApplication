import datetime
import tkinter
import tkinter.messagebox
import customtkinter as ct
import os
import pickle
import time

Waittime=6480000#Time Range that program will toggled off already marked companies by itself so that you could reapply

ct.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ct.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
dictoggle={};dicposition={};dictime={}#for the purpose of sorting and toggling logic
GroupedLi=[]
class wind(ct.CTk):
    
    def __init__(self):
        global dictoggle,dicposition,dictime,GroupedLi
        super().__init__()
        
        self.title("RandomBullshatGO")
        self.geometry(f"{1100}x{580}")
        #self.resizable(False, False)
 
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure((0,1,2), weight=1)

        #firstframe
        self.SideFrame= ct.CTkFrame(self,width=150,corner_radius=0)
        self.SideFrame.grid(row=0,column=0,rowspan=3,sticky='nsew')
        self.SideFrame.grid_columnconfigure((0),weight=1)
        self.SideFrame.grid_rowconfigure(1,weight=1)

        
        self.logo_label = ct.CTkLabel(master=self.SideFrame, text="Vuong Duong", font=ct.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.scrollable_frame = ct.CTkScrollableFrame(master=self.SideFrame, label_text="Application List")
        self.scrollable_frame.grid(row=1, column=0,rowspan=4,columnspan=4, padx=(0, 0), pady=(10, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        self.scrollable_frame_switches = []
        #scrollable list content
        with open(r"D:\Largecodefile\TkinterApply\List1.txt",'r') as f:
            Lines=f.read().splitlines()        
        for i,val in enumerate(Lines):
            switch = ct.CTkSwitch(master=self.scrollable_frame, text=val,command=lambda charac=val , index=i: self.changestate(charac,index))#lambda index=i: self.changestate(index)
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)


        #secondframe
        self.MainFrame= ct.CTkFrame(self,fg_color='transparent')
        self.MainFrame.grid(row=0,column=1,sticky='nsew')
        self.MainFrame.grid_rowconfigure((0,1,5,6,7), weight=1)
        self.MainFrame.grid_columnconfigure((0), weight=1)
        self.sortratio=ct.CTkOptionMenu(master=self.MainFrame, values=["Not Yet Applied", "Nearest Reset Time","Applied", "Furthest Reset Time","Lexicographically"],command=self.sortevent)
        self.sortratio.grid(row=0,column=0,pady=(20,0),sticky='n')
        self.typer= ct.CTkTextbox(master=self.MainFrame,corner_radius=10,height=350)
        self.typer.grid(row=1,column=0,rowspan=3,padx=(10,10),sticky='nsew')
        self.submit1=ct.CTkButton(master=self.MainFrame,text="Submit",corner_radius=10)
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
        with open(r"D:\Largecodefile\TkinterApply\Logging.txt",'r') as f:
            Lines2=f.readlines()
            curprint="".join(Lines2)
            self.SideBox1.insert("0.0",curprint)
            self.SideBox1.configure(state='disabled')

        #Retrieve Pickle dictionary data  for True and False state of Switch
        with open(r"D:\Largecodefile\TkinterApply\dictionstoring.txt", "rb") as f:#dictionary to keep track of true false state
            GroupedLi=pickle.load(f)
        times=time.time()
        dictoggle,dicposition,dictime=GroupedLi[0],GroupedLi[1],GroupedLi[2]
        scanli1=[i for i in dictoggle if dictoggle[i] == True]#get key in dic with specific value IE (if got toggle on: in this case 1)
        scanli2=[i for i in dictime if dictime[i] !=0 and times>dictime[i]]
        if len(scanli1) !=0:
            for i in scanli1:
                self.scrollable_frame_switches[dicposition[i]].select()
        if len(scanli2) !=0:
            print(scanli2)
            for i in scanli2:
                dictime[i]=0
                log=f'Toggled off value of {str(i)} since the amount of time f{str(Waittime)} has been met\n\n'
                self.logging(log)
                self.scrollable_frame_switches[dicposition[i]].toggle()#deselect if specific time of daterange meet: in this case, set as 75 days from the time of checking     

    def sortevent(self,currentval):# Sorting
        print(currentval)
        return currentval
    
    def logging(self, logger):
        with open(r"D:\Largecodefile\TkinterApply\Logging.txt",'a') as f:#change from 'a' to 'w' if prefre one-time logfile, IE session log, meaning full log will not exist when program end
            self.SideBox1.configure(state='normal')
            f.writelines(logger)

            #self.SideBox1.delete("0.0","100.0")
            self.SideBox1.insert("0.0",logger)
            self.SideBox1.configure(state='disabled')

    def changecolor(self,setc : str): #Set Appearance Mode
        ct.set_appearance_mode(setc.lower())
    
    def Delcontent(self):#Content Delete Function
        dialog = ct.CTkInputDialog(text="Input Company Name:", title="Janitor")
        print("Return Val:", dialog.get_input())

    def changestate(self,val,index):#toggle switch 
        dictoggle[val]=not dictoggle[val]
        log=f'Switched value of {str(val)} to {str(dictoggle[val])}\n\n'
        self.logging(log)
        if dictoggle[val] == True:
            dictime[val]=time.time()+Waittime
        GroupedLi=[dictoggle,dicposition,dictime]
        with open(r"D:\Largecodefile\TkinterApply\dictionstoring.txt", "wb") as f:
            pickle.dump(GroupedLi, f)

    
if __name__ == "__main__":
    app = wind() 
    app.mainloop()
