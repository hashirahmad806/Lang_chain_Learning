from groq.resources import Embeddings
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


#  Generate the meta Data  tagger from  Langchain

# lets  suppose we are  useing the openAi one

from langchain_cummunity.documeny_transformers.openai_functions import(create_metadata_tagger)

from langchain_openai import ChatOpenAIenai




text_splitter = RecursiveCharacterTextSplitter(
    chunk_size =500 ,
    chunk_overlap = 150
)

schema ={
    "properties" : {
      "title"  :{ "type" : "String"},
      "keyword": { "type" : "array" , "items" :{"type" :"String"} } ,
      "hasCode" :{"type" : "boolean"}   
    },

    "required" : ["title" , "keywords" , "hasCode"]
}

llm = ChatOpenAI(openai_api_key = key_param.openai_api_key , 
temperature =1,
model ="gpt-4"

)

documents_transformer = create_metadata_tagger(metadata_schema =schema  , llm  =llm)

docs = documents_transformer.transform_documents(cleaned_pages)

slpit_docs =text_splitter.split_documents(docs)

print(split_docs[0])



# Now  Generating The  Embeddings from the  from the  Chunks 

# we use let  openai model for the Embeddings


from langchain_openai import OpenAIEmbeddings
from langchain_mongodb  import MongoDBAtlasVectorSearch


embeddings =OpenAIEmbeddings(openai_api_key =key_param.openai_api_key)

vector_store = MongoDBAtlasVectorSearch.from_documents(split_docs , embeddings , collection = collection)

#  How to  improveRAG system in real time, you need an event-driven ingestion pipeline that automatically processes changes as they happen, rather than relying only on scheduled batch jobs (like the cronjobs or scheduled Atlas Triggers




















