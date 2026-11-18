from pymongo import MongoClient
from langchain_cummunity.document_loaders import PyPDFLoader

from dotenv import load_dotenv
load_dotenv()

#  location of pdf
loader =PyPDFLoader('./sample_files/mongodb.pdf')

# load the  pages of pdf books
pages =loader.load()
#  lets print the  First page of the pdf
print(pages[0])
#    Preprocessing  of the  Start  Here  before Embeddings

#  now  we have load the data or books  now  Sanitizing Data
#  Sanitizing  means ====>  Removing the  any Sensitive   Data  or  junks  and empty and unnecessary Data 
#  these   Steps  can be  done  Before the  Embedding to the Vector   

#  pdf scaniting is  different  from  stracture Html

#  Step  1   convert  everything  to the Same Formate
#   Create  clean page array
cleaned_pages =[]

for page in pages :
    if len(page.page_content.split("") ) > 20 :  # if page length is greater then 20 then     #
        cleaned_pages.append   # add to the  clean array (page)
