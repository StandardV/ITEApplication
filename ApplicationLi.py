import threading
import pickle
import os
import time
import customtkinter as ct
import ApplicationSorter
from multiprocessing import Pool
from ctk_entryframe import CTkEntryFrame
from smallServer import Searchfunction

import webbrowser
import winreg

# try:
#     import httplib  # python < 3.0
# except:
#     import http.client as httplib




ct.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ct.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class GOTOWORKPEOPLE(ct.CTk):
    """Provide customtkinter Gui"""
    def __init__(self):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        #backend_path = os.path.join(current_dir,"smallServer")
        self.name_search_function = Searchfunction.COMPANYPARSER()
        self.hyperlink_count =0

        self.name='Vuong Duong' #Change this for changing users name
        self.default_state='Lexicographically'
        self.default_check_option = "Display all"# for applying mode
        self.wait_time=6480000#Time Range that program will toggled off
                                #already marked companies by itself so that you could reapply
        self.company_path= os.path.join(current_dir, "List1.txt")
        #r"D:\Largecodefile\TkinterApply\List1.txt"#This path point to List1
        self.log_path = os.path.join(current_dir, "Logging.txt")
        #r"D:\Largecodefile\TkinterApply\Logging.txt"#This path point to Log file
        self.dictionary_path = os.path.join(current_dir, "dictionstoring.txt")
        #r"D:\Largecodefile\TkinterApply\dictionstoring.txt"# This path point to dictionstoring
        self.dictoggle={}
        self.dicposition={}
        self.dictime={}#for the purpose of sorting and toggling logic
        self.grouped_li=[]



        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"HTTP\shell\open\command")
        default_browser_path = winreg.QueryValue(key, None)

        # Clean up the path (remove quotes and any additional arguments)
        self.default_browser_path = default_browser_path.split('"')[1]
        webbrowser.register('my_browser', None, webbrowser.BackgroundBrowser(self.default_browser_path))
        print(self.default_browser_path)


        self.title("ITEApplication.py")
        self.geometry(f"{1200}x{750}")
        #self.resizable(False, False)

        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure((0,1,2), weight=1)

        #firstframe
        self.SideFrame= ct.CTkFrame(self,
                                    width=150,
                                    corner_radius=0)

        self.SideFrame.grid(row=0,
                            column=0,
                            rowspan=3,
                            sticky='nsew')

        self.SideFrame.grid_columnconfigure((0),weight=1)

        self.SideFrame.grid_rowconfigure(1,weight=1)


        self.logo_label = ct.CTkLabel(master=self.SideFrame,
                                      text=self.name,
                                      font=ct.CTkFont(size=20, weight="bold"))

        self.logo_label.grid(row=0,
                             column=0,
                             padx=20,
                             pady=(20, 10))

        self.scrollable_frame = ct.CTkScrollableFrame(master=self.SideFrame,
                                                      label_text="Application List")
        self.scrollable_frame.grid(row=1,
                                   column=0,
                                   rowspan=4,
                                   columnspan=4,
                                   padx=(0, 0),
                                   pady=(10, 0),
                                   sticky="nsew")

        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        self.scrollable_frame_switches = []
        #scrollable list content
        with open(self.company_path,'r') as f:
            self.company_display_track=f.read().splitlines()

        for i,val in enumerate(self.company_display_track):
            switch = ct.CTkSwitch(master=self.scrollable_frame,
                                  text=val,command=lambda charac=val,
                                  index=i: self.changestate(charac,index))#lambda index=i: self.changestate(index)
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)


        #secondframe
        self.MainFrame= ct.CTkFrame(self,fg_color='transparent')

        self.MainFrame.grid(row=0,column=1,sticky='nsew')

        self.MainFrame.grid_rowconfigure((0,1,5,6,7), weight=1)

        self.MainFrame.grid_columnconfigure((0), weight=1)

        self.sortratio=ct.CTkOptionMenu(master=self.MainFrame,
                                        values=["Lexicographically","Not Yet Applied","Applied"],
                                        command=self.sortevent)

        self.sortratio.grid(row=0,
                            column=0,
                            pady=(20,5),
                            sticky='n')


        self.typer= ct.CTkTextbox(master=self.MainFrame,
                                  corner_radius=10,
                                  height=350)#middle input box

        self.typer.grid(row=1,
                        column=0,
                        rowspan=3,
                        padx=(10,10),
                        sticky='nsew')

        self.submit1=ct.CTkButton(master=self.MainFrame,
                                  text="Submit",
                                  corner_radius=10,
                                  command=self.trigger_testing)

        self.submit1.grid(row=5,
                          column=0,
                          pady=20,
                          sticky='ns')

        self.DiagBox1 = ct.CTkButton(master=self.MainFrame,
                                     text="Delete Content",
                                     corner_radius=10,
                                     command=self.del_content)

        self.DiagBox1.place(relx=0.5, rely=0.5, anchor=ct.CENTER)

        self.DiagBox1.grid(row=6,column=0,pady=0,sticky='ns')

        self.Progress1=ct.CTkProgressBar(master=self.MainFrame)

        self.Progress1.grid(row=7,column=0,padx=10,pady=30,sticky='s')

        self.Progress1.configure(mode="indeterminnate")

        self.Progress1.start()

        #thirdFrame
        self.SideFrame2 = ct.CTkFrame(self)
        self.SideFrame2.grid(row=0,column=2,sticky = 'nsew')
        self.SideFrame2.columnconfigure(0,weight=1)
        self.SideFrame2.rowconfigure((1),weight=1)


        self.colorchanger1=ct.CTkOptionMenu(master=self.SideFrame2,
                                            values=["Dark","Light"],
                                            command=self.changecolor)

        self.colorchanger1.grid(row=0,column=0,padx=5,pady=5,sticky='nsew')

        self.sort_apply_event=ct.CTkOptionMenu(master=self.SideFrame2,
                                               values=["Display all",
                                                       "Display Top Option",
                                                       "Auto Open Page"],
                                               command=self.parsing_event)

        self.sort_apply_event.grid(row=2,column=0,padx=5,pady=5,sticky='new')

        self.SideBox1=ct.CTkTextbox(master=self.SideFrame2,
                                    text_color='gray')#right side config box  , height=150
        
        self.SideBox1.grid(row=1, column=0, padx=5, pady=(0, 0), sticky='nsew')
        
        #self.SideBox1.bind("<Button-1>", self.open_hyperlink)

        #self.right_side_box2=ct.CTkTextbox(master=self.SideFrame2,text_color='gray')#right side config box
        #self.right_side_box2.grid(row=3,column=0,padx=5,pady=(0,5),sticky='nsew')

        #log content
        with open(self.log_path,'r') as f:
            Lines2=f.readlines()
            curprint="".join(Lines2)
            self.SideBox1.insert("0.0",curprint)
            self.SideBox1.configure(state='disabled')

        #Retrieve Pickle dictionary data  for True and False state of Switch
        with open(self.dictionary_path, "rb") as f:#dictionary to keep track of true false state
            self.grouped_li=pickle.load(f)
        times=time.time()
        self.dictoggle,self.dicposition,self.dictime=self.grouped_li[0],self.grouped_li[1],self.grouped_li[2]
        self.scanli1=[i for i in self.dictoggle if self.dictoggle[i] is True]
        #get key in dic with specific value IE (if got toggle on: in this case 1)
        self.scanli2=[i for i in self.dictime if self.dictime[i] !=0 and times>self.dictime[i]]
        if len(self.scanli1) !=0:
            for i in self.scanli1:
                self.scrollable_frame_switches[self.dicposition[i]].select()
        if len(self.scanli2) !=0:
            print(self.scanli2)
            for i in self.scanli2:
                #self.dictime[i]=0
                log=f'System: Toggled off value of {str(i)} since the amount of time {str(self.wait_time)} has been met\n\n'
                self.logging(log)
                self.scrollable_frame_switches[self.dicposition[i]].toggle()
                #deselect if specific time of daterange meet: in this case, set as 75 days from the time of checking


    def trigger_testing(self):
        """action when press trigger testing"""
        if len(self.typer.get("1.0",'end-1c'))>0:
            temp=[part for part in self.typer.get("1.0",'end-1c').split('\n') if part != '']
            #extracting the text entered into the typer textbox in the GUI
            print(temp)
            temp = [i for i in temp if i not in self.dictoggle]
            #remove data if the insert value is duplicate
            with open(self.company_path,'a') as f:
                for i in temp:
                    f.write(f'{i}\n')
                    self.dictoggle[i]=False
                    self.dictime[i]=0#modify self.dictime and self.dictoggle
            log=f'Added {temp} to the System\n\n'
            self.logging(log)
            self.typer.delete("1.0",'end')
            self.company_display_track, self.dicposition=ApplicationSorter.sortLexico()
            #ADD IN self.dicposition
            Li=[self.dictoggle,self.dicposition,self.dictime]
            with open(self.dictionary_path, "wb") as k:
                print('accessed')
                pickle.dump(Li, k)
            self.sortevent(self.default_state)


        #self.logging()
    def sortevent(self,currentval):# Sorting
        """sort mode for value"""
        self.default_state= currentval
        self.scanli1=[i for i in self.dictoggle if self.dictoggle[i] is True]
        if currentval == 'Lexicographically':
            temp=self.company_display_track
        elif currentval == 'Applied':
            temp=self.scanli1
        else:
            temp=[i for i in self.company_display_track if i not in self.scanli1]
        self.scrollable_frame.destroy()
        self.scrollable_frame = ct.CTkScrollableFrame(master=self.SideFrame,
                                                      label_text="Application List")
        self.scrollable_frame.grid(row=1,
                                   column=0,
                                   rowspan=4,
                                   columnspan=4,
                                   padx=(0, 0),
                                   pady=(10, 0),
                                   sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        tempLi={}
        for i,val in enumerate(temp):
            tempLi[val]= i
        for i,val in enumerate(temp):
            switch = ct.CTkSwitch(master=self.scrollable_frame,
                                  text=val,command=lambda charac=val,
                                  index=i: self.changestate(charac,index))#lambda index=i: self.changestate(index)
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)
        if len(self.scanli1) !=0 and currentval != 'Not Yet Applied':
            for i in self.scanli1:
                self.scrollable_frame_switches[tempLi[i]].select()

    def parsing_event(self, selected_value:str):
        """switch value of auto parser for opening mode"""
        self.default_check_option = selected_value
        self.logging(f"Apply Mode is now{selected_value}\n\n")


    def change_apply_mode(self,apply_mode):# Sorting
        """change apply mode for the model"""
        self.default_check_option = apply_mode

    def logging(self, logger:str):
        """Write down for log info"""
        with open(self.log_path,'a') as f:
            #change from 'a' to 'w' if prefre one-time logfile,
            # IE session log, meaning full log will not exist when program end
            self.SideBox1.configure(state='normal')
            f.writelines(logger)

            #self.SideBox1.delete("0.0","100.0")
            self.SideBox1.insert("0.0",logger)
            self.SideBox1.yview_moveto(0.0)
            self.SideBox1.configure(state='disabled')

    def changecolor(self, setc : str): #Set Appearance Mode
        """change color on application appearance"""
        ct.set_appearance_mode(setc.lower())

    def del_content(self):#Content Delete Function
        """pop off box to delete content"""
        while True:
            dialog = CTkEntryFrame(text="Input Company Name:", title="Janitor")
            temp=''
            temp=dialog.get_input()
            if temp is not None:
                if temp != '' or temp != ' ':
                    if self.dicposition.get(temp,-1) !=-1:
                        self.dictime.pop(temp)
                        self.dictoggle.pop(temp)
                        self.company_display_track,self.dicposition=ApplicationSorter.delvalue(temp)
                        log=f'Deleted all instances of "{temp}" from the System\n\n'
                        self.logging(log)
                        Li=[self.dictoggle,self.dicposition,self.dictime]
                        with open(self.dictionary_path, "wb") as k:
                            print('accessed')
                            pickle.dump(Li, k)
                        self.sortevent(self.default_state)
                else:
                    print('No value returned')
            else:
                print('value canceled')
                break


    def startthread(self,val,index):#toggle switch
        """Change state in company tick box"""
        self.dictoggle[val]=not self.dictoggle[val]
        log=f'Switched value of {val} to {self.dictoggle[val]}\n\n'
        #run company name from here to link select model
        #do a call that check for current DEFAULT_CHECK_OPTION here to do function
        self.logging(log)
        if self.dictoggle[val] is True:
            self.dictime[val]=time.time()+self.wait_time#assign auto turning off time

        try:
            self.display_company_classification(val)
        except Exception as e:
            print('exception at',e)

        else:
            self.dictime[val]=0
        self.grouped_li=[self.dictoggle,self.dicposition,self.dictime]
        with open(self.dictionary_path, "wb") as f:
            pickle.dump(self.grouped_li, f)

    def changestate(self,val,index):
        """call thread for company name processing"""
        thread = threading.Thread(target = self.startthread, args = (val,index),daemon=True)
        thread.start()

    def display_company_classification(self,company_name):
        """verify company URL and run a ranking model"""
        #search_function_results in form of a dictionary
        search_function_results = {}
        search_function_results = self.name_search_function.run(company_name)

        #print("I came to the function")
        match self.default_check_option:
            case "Display all":#parse through all items and print each key values pair
                #print("access display all")
                #print(search_function_results)
                self.logging("\n")#add in a space at the end for better visualization
                for key, values in search_function_results.items():
                    if len(values) >0:
                        for value in values:
                            self.insert_hyperlink(value,value)
                        self.logging(key)
                #development, caching the value incase it will be re-toggled


            case "Display Top Option":
                self.logging("\n")#add in a space at the end for better visualization
                for key, values in search_function_results.items():
                    if len(values) >0:
                        self.insert_hyperlink(values[0],values[0])#sorting best later
                        self.logging(key)
                #pick the shortest, but also pick the most matching,
                #      most matching should take priority
                #display 1 of each type, prioritize the smallest len,


                #development, caching the value incase it will be re-toggled

            case "Auto Open Page":
                for key, values in reversed(list(search_function_results.items())):
                    if len(values) >0:
                        hyperlink_text = values[0]#sorting best later
                        webbrowser.get('my_browser').open(hyperlink_text, new=0)
                        break
                #auto open in the order set in the dict,
                # prioritize value in front since it's more accurate
                

    def insert_hyperlink(self, text, url):
        """insert hyperlink to user logger"""#put url into text and url
        self.SideBox1.configure(state='normal')
        self.hyperlink_count += 1  # Increment counter
        tag_name = f"hyperlink_{self.hyperlink_count}"
        self.SideBox1.insert("0.0", "\n"+text+"\n", tag_name)
        # Insert text with "hyperlink" tag

        # Bind event to open URL on click
        self.SideBox1.tag_bind(tag_name, "<Enter>",
                               lambda event: self.SideBox1.configure(cursor="hand2"))

        self.SideBox1.tag_bind(tag_name, "<Leave>",
                               lambda event: self.SideBox1.configure(cursor="arrow"))

        self.SideBox1.tag_bind(tag_name, "<Button-1>",
                               lambda event, url=url: self.open_hyperlink(event, url))

        self.SideBox1.tag_config(tag_name, foreground="blue")

        self.SideBox1.configure(state='disabled')


    def open_hyperlink(self, event, url=None):
        """open link with user default browser"""
        index = self.SideBox1.index("@%s,%s" % (event.x, event.y))
        tag_name = self.SideBox1.tag_names(index)[0]  # Get the first tag

        if tag_name.startswith("hyperlink_"):
            ranges = self.SideBox1.tag_ranges(tag_name)
            if ranges:
                start, end = ranges[0], ranges[1]
                hyperlink_text = self.SideBox1.get(start, end)
                #print(hyperlink_text)

                webbrowser.get('my_browser').open(hyperlink_text, new=0)
                #webbrowser.open(hyperlink_text,new=0)

    # def have_internet(self) -> bool:
    #     """verify for internet"""
    #     conn = httplib.HTTPSConnection("8.8.8.8", timeout=5)
    #     try:
    #         conn.request("HEAD", "/")
    #         return True
    #     except Exception:
    #         print(Exception)
    #         return False
    #     finally:
    #         conn.close()

if __name__ == "__main__":
    app = GOTOWORKPEOPLE()
    app.mainloop()
    