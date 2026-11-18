# oad_data.py file

# This code ingests a pdf, removes empty pages, chunks the pages into paragraphs, generates metadata for the chunks, creates embeddings, and stores the chunks and their embeddings in a MongoDB collection.

# The embedding model used in the examples below is the voyage-3.5-lite. The voyage-3.5-litemodel from Voyage AI is a state-of-the-art embedding model designed for efficient and high-quality text retrieval. It supports multiple embedding dimensions—2048, 1024, 512, and 256—and offers various quantization options, including int8 and binary. Voyage-3.5-lite is suitable for a wide range of domains, such as technical documentation, code, law, finance, web reviews, long documents, and conversations.

# To get started with Voyage AI, check out the Voyage AI documentation.














from pymongo import MongoClient
from langchain_openai import ChatOpenAI
from langchain_voyageai import VoyageAIEmbeddings
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_transformers.openai_functions import (
    create_metadata_tagger,
)

import key_param



# Set the MongoDB URI, DB, Collection Names

client = MongoClient(key_param.MONGODB_URI)
dbName = "book_mongodb_chunks"
collectionName = "chunked_data"
collection = client[dbName][collectionName]

loader = PyPDFLoader(".\sample_files\mongodb.pdf")
pages = loader.load()
cleaned_pages = []

for page in pages:
    if len(page.page_content.split(" ")) > 20:
        cleaned_pages.append(page)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=150)

schema = {
    "properties": {
        "title": {"type": "string"},
        "keywords": {"type": "array", "items": {"type": "string"}},
        "hasCode": {"type": "boolean"},
    },
    "required": ["title", "keywords", "hasCode"],
}

llm = ChatOpenAI(
    openai_api_key=key_param.LLM_API_KEY, temperature=0, model="gpt-3.5-turbo"
)

document_transformer = create_metadata_tagger(metadata_schema=schema, llm=llm)

docs = document_transformer.transform_documents(cleaned_pages)

split_docs = text_splitter.split_documents(docs)

embeddings = VoyageAIEmbeddings(voyage_api_key=key_param.VOYAGE_API_KEY, model="voyage-3.5-lite")


vectorStore = MongoDBAtlasVectorSearch.from_documents(
    split_docs, embeddings, collection=collection
)
