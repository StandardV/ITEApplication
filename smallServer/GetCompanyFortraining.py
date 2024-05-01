"""Pull company from file out to run through link search"""
import csv
from googlesearch import search

#from openai import OpenAI



# to search
#client = OpenAI( api_key = "sk-proj-R7PFo3IrqlgPLe3Gr8KhT3BlbkFJQqg1LMLp7mvcWmuR3176")
PathList1=r"D:\Largecodefile\TkinterApply\List1.txt"#This path point to List1
csv_path = r"C:\Users\duong\OneDrive\Desktop\Automations\Webdevelopment\Largecodefile\smallServer\DatasetCompany.csv"

QUERY = "BlackPearl Technology"
QUERY_ADD = " careers"
links = []

def quick_goog_search(QUERY,links:list):
    """perform search to append"""
    QUERY += QUERY_ADD
    
    for j in search(QUERY, tld="co.in", num=10, stop=10, pause=2):
        links.append(j)
    for j in links:
        print(j)

with open(PathList1,"r") as fp:
    Lines = fp.readlines()
    
    for line in Lines:
        
        temp_company_name = ""
        for i in line:
            if i == "(" or i== "\r":
                break
            else:
                temp_company_name+=str(i)
        print("Working on ",QUERY)
        QUERY = temp_company_name
        quick_goog_search(QUERY,links)



with open(csv_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Writing header
    writer.writerow(['Hyperlink'])
    
    # Writing data
    for item in links:
        writer.writerow([item])
#prioritize mainsite, linkedin. not some review site
#run j to an llm, pick out legitimate option, might be 2, if need more the system can assign point and extend it to be 3
#can take full view of page for llm to analyze too to see if it lead to the right one, but it's optional and can be use for auto apply task

#LINK_LIST = '\n'.join(str(links))


# prompt = f"inspect these link and give me top 3 link classified into orders, 1st: company career page , 2nd: company linkedin(both main page and career page is acceptable), 3rd: company direct websitethe company name is : {QUERY} link list{LINK_LIST}do remember to parse the site and verify, not just check the hyperlinkdo verify company career page location if within US, if not, discard, if doubt : put a mark (might not be in US)do not out put unecessary details, just what you're asked to do"

# chat_completion = client.chat.completions.create( 
# 	messages = [ {"role": "system",
#                	  "content":  prompt} ],                   
                                      
# 	model="gpt-3.5-turbo"
# ) 

# print(chat_completion.choices[0].message.content) 


