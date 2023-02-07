import datetime
import tkinter
import tkinter.messagebox
import customtkinter as ct
import os
import time

ct.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ct.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class wind(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("RandomBullshatGO")
        self.geometry(f"{1100}x{580}")
 
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure((0,1,2,3), weight=1)

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


        with open(r"D:\Largecodefile\TkinterApply\List1.docx",'r') as f:
            Lines=f.read().splitlines()
        for i,val in enumerate(Lines):
            switch = ct.CTkSwitch(master=self.scrollable_frame, text=val)
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)

        #secondframe
        self.MainFrame= ct.CTkFrame(self,fg_color='transparent')
        self.MainFrame.grid(row=0,column=1,sticky='nsew')
        self.MainFrame.grid_rowconfigure((0,1,3), weight=0)
        self.MainFrame.grid_columnconfigure((0), weight=1)
        self.sortratio=ct.CTkOptionMenu(master=self.MainFrame, values=["Not Yet Applied", "Nearest Reset Time","Applied", "Furthest Reset Time","Lexicographically"],command=self.sortevent)
        self.sortratio.grid(row=0,column=0,pady=20,sticky='n')
        self.typer= ct.CTkTextbox(master=self.MainFrame,corner_radius=10,height=350)
        self.typer.grid(row=1,column=0,padx=(10,10),sticky='nsew')
        self.submit1=ct.CTkButton(master=self.MainFrame,text="Submit",corner_radius=10)
        self.submit1.grid(row=3,column=0,pady=10,sticky='ns')
        self.Progress1=ct.CTkProgressBar(master=self.MainFrame)
        self.Progress1.grid(row=4,column=0,padx=10,pady=20,sticky='nsew')
        self.Progress1.configure(mode="indeterminnate") 
        self.Progress1.start()




    def fillspace(self,curlength):
        space=" "
        temp=32-curlength
        return space*temp

    def sortevent(self,currentval):
        print(currentval)
        return currentval

if __name__ == "__main__":
    app = wind() 
    app.mainloop()
