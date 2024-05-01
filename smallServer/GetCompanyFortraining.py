"""Pull company from file out to run through link search"""
import csv
from googlesearch import search
import os
#from openai import OpenAI


current_dir = os.path.dirname(os.path.abspath(__file__))

PathList1 = os.path.join(current_dir, "List1.txt")
csv_path = os.path.join(current_dir, "DatasetCompany.csv")

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


