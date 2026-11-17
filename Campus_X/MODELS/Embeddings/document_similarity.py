# from langchain_huggingface import HuggingFaceEmbeddings
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity
# from dotenv import load_dotenv
# load_dotenv()
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# documents = ['Harnessing green electricity from sunlight relies heavily on silicon wafer modules. Once sunlight hits the cells, the energy excites particles to create voltage. Modern clean-energy grids feed this generated DC electricity through central inverters to supply alternating current to homes and commercial facilities.']

# sentences = {
#     "doc_1": "The dog chased the cat across the garden.",
#     "doc_2": "A hound ran after a feline through the yard.",
#     "doc_3": "Quarterly earnings exceeded expectations with massive revenue growth.",
#     "doc_4": "The firm laid off staff to avoid bankruptcy.",
#     "doc_5": "I forgot my account credentials and need to reset my password.",
#     "doc_6": "The forecast calls for heavy rain and thunderstorms tomorrow.",
# }

# query = "How does solar energy work?"

# #  for the  first document, we can compute the similarity score with the query
# query_embedding = embeddings.embed_query(query)
# document_embeddings = [embeddings.embed_query(doc) for doc in documents]

# #   for the sentences, we can compute the similarity scores with the sentences

# ques = 'User cannot sign into the system.'
# question_embedding = embeddings.embed_query(ques)
# sentence_embeddings = [embeddings.embed_query(sentence) for sentence in sentences.values()]

# #  for  the first document, we can compute the similarity score with the query

# similarity_scores = cosine_similarity(
#     [query_embedding], document_embeddings)[0]
# print("Similarity Scores:")
# for i, score in enumerate(similarity_scores):
#     print(f"Document {i+1}: {score}")

# # for the sentences, we can compute the similarity scores with the sentences


# Similarity_scores_sentences = cosine_similarity(
#     [question_embedding], sentence_embeddings)[0]
# print("Similarity Scores (Sentences):")
# for i, score in enumerate(Similarity_scores_sentences):
#     print(f"Sentence {i+1}: {score}")

import os
import numpy as np
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

# 1. Initialize the embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 2. Data
sentences = {
    "doc_1": "The dog chased the cat across the garden.",
    "doc_2": "A hound ran after a feline through the yard.",
    "doc_3": "Quarterly earnings exceeded expectations with massive revenue growth.",
    "doc_4": "The firm laid off staff to avoid bankruptcy.",
    "doc_5": "I forgot my account credentials and need to reset my password.",
    "doc_6": "The forecast calls for heavy rain and thunderstorms tomorrow.",
}

# 3. Query
query = "User cannot sign into the system."

# --- BATCH EMBEDDING ---
# Use embed_documents() instead of a list comprehension with embed_query()
# This embeds all items in a single GPU/CPU batch (much faster).
keys = list(sentences.keys())
texts = list(sentences.values())

sentence_embeddings = embeddings.embed_documents(texts)
query_embedding = embeddings.embed_query(query)

# --- COSINE SIMILARITY ---
scores = cosine_similarity([query_embedding], sentence_embeddings)[0]

# --- PAIR SCORES WITH DICTIONARY KEYS & SORT ---
results = [
    {"id": doc_id, "score": score, "text": text}
    for doc_id, score, text in zip(keys, scores, texts)
]

# Sort descending by similarity score
results.sort(key=lambda x: x["score"], reverse=True)

print(f"Query: \"{query}\"\n")
print(f"{'Rank':<5} {'ID':<8} {'Score':<8} {'Text'}")
print("-" * 75)
for rank, item in enumerate(results, start=1):
    print(
        f"{rank:<5} {item['id']:<8} {item['score']:.4f}   {item['text'][:50]}..."
    )
c
