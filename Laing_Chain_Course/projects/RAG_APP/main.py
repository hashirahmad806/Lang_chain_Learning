from h11._abnf import chunk_size
from pymongo import MongoClient
from langchain_cummunity.document_loaders import PyPDFLoader

#  for text split we use TextSplittering 
from langchain.text_splitter import RecursiveCharacterTextSplitter


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

print(cleaned_pages[0])


#  now have data   lets  Chunk it  
#  Chunk means ===>  Breaking the  larger text into small pieces
#  To efficiently  index  and  Search Data
#  you  can chunk data by 
#  Sentences or  paragraph or  page or section or semantically

#  Now How  to U know which chunks methods is  return Good  Result  so u need  experiment
# apply  all the term which can give u good   result 



text_splitter = RecursiveCharacterTextSplitter(
    chunk_size =500 ,
    chunk_overlap = 150
)
split_docs = text_splitter.split_documents(cleaned_pages)

print(split_docs[21])


#  Generate the