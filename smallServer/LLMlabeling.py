"""Use company link for classification to open website"""
from meta_ai_api import MetaAI
import csv
import os
import pyperclip


def multi_input(links):
    """multi line input"""

    print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    contents = []

    while True:#take multi lines input in terminal
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    if 'printinput' in contents:
        print(links)
        multi_input(links)
    return contents
links = []
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir,"DatasetCompany.csv")
#r"C:\Users\duong\OneDrive\Desktop\Automations\Webdevelopment\Largecodefile\smallServer\DatasetCompany.csv"
ai = MetaAI()


with open(csv_path, 'r', newline='') as file:
    reader = csv.reader(file)
    Lines = list(reader)
while True:
    print("Enter start and end input:", end =" ")

    x = input()
    print("")
    u, v = map(int, x.split("-"))
    #print(Lines)
    links = [sublist[0] for sublist in Lines[abs(u):abs(v)]]    #Lines[abs(u):abs(v)][0]

    #print(links)

    LINK_LIST = '\n'.join(links)
    prompt = LINK_LIST+"\n\ninspect these link and give me top 3 link classified into orders, company career page , company linkedin(both main page and career page is acceptable), company direct website do remember to parse the site and verify, not just check the hyperlinkdo verify company career page location if within US, if not, discard, if doubt : put a mark (might not be in US),if unrelated sites to what I mention including but not limited to, forum, a mention from some different page, an employee saying the name on social media, put it as 'Others'do not out put unecessary details, only 4 tags type as mentioned and they have to be repetitive for each of the hyperlink, just what you're asked to do you dont need to repeat the link, just give me the classification in the order they are put in to save token amount. Just classify, and give new line for each classification DO NOT EXPLAIN. MOST IMPORTANT:   DO NOT REPEAT THE LINK DO NOT HALLUCINATE, I MEAN, ONLY GIVE THE CLASSIFICATION RESULT, DO NOT TRY TO GIVE 3 IF ONLY ASKED FOR 2"

    print(LINK_LIST)
    pyperclip.copy(prompt)
    #response = ai.prompt(message=prompt)
    #print(response['message'])

    contents = multi_input(links)
    print(contents,"\n","last input is",u,"-",v)

    for count, i in enumerate(range(u, v)):
        if len(Lines[i]) == 1:
            Lines[i].append(contents[count])
        else:    
            Lines[i][1] = contents[count]#need to fix bug here, write in a cell that column haven't been made yet

    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(Lines)
