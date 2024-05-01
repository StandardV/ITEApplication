"""Quicksearch tool for jobs"""
import os
import joblib
from googlesearch import search
from sklearn.feature_extraction.text import TfidfVectorizer

class COMPANYPARSER():
    """parse company name and run it through model classifer"""
    def __init__(self):
        #threading.Thread.__init__(self, daemon=True)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.query = "BlackPearl Technology"
        self.model_path = os.path.join(current_dir,"hyperlinkclassification.pkl")

        with open(self.model_path, "rb") as f:
            hyperlink_classifier = joblib.load(f)

        self.trained_model_classifier = hyperlink_classifier[0]
        self.tfidf_vectorizer = hyperlink_classifier[1]#vectorizer


    def name_parsing(self,company):
        """parse through name with given string"""
        self.query = company
        query_add = " careers"
        self.query += query_add

        links = []
        for j in search(self.query, tld="co.in", num=10, stop=10, pause=2):
            links.append(j)
        return links
        #LINK_LIST = '\n'.join(str(links))


    def model_prediction(self,hyperlink_list:list):
        """run parsed links through model"""
        predict_result = {'Others':[],
                          'Company Direct Website':[],
                          'Company LinkedIn':[],
                          'Company Career Page':[]}
        for i in hyperlink_list:
            new_samples_tfidf  = self.tfidf_vectorizer.transform([i ])
            labels_prediction  = self.trained_model_classifier.predict(new_samples_tfidf)

            #labels_prediction = str(labels_prediction)
            #convert to string for predict_result matching,
            #       could keep it to write to csv for retraining

            predict_result[labels_prediction[0]].append(i)
            #append links to list that matched the prediction

        return predict_result


    def name_process_n_parsing(self, name_input):
        """parse input name and run it through model"""
        temp_company_name = ""
        print(name_input)
        for char in name_input:
            if char == "(":
                break
            else:
                temp_company_name+=str(char)
        return self.name_parsing(temp_company_name)


    def run(self, name_input:str):
        """run the threading"""
        # Override the run method to perform threading operations
        # You can call the methods you want to run concurrently here
        return  self.model_prediction(self.name_process_n_parsing(name_input))
