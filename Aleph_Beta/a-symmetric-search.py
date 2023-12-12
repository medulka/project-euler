#!usr/bin/env python3
"""
Symmetric and asymmetric semantic search
after: https://github.com/Aleph-Alpha/examples/blob/main/boilerplate/04_semantic_search.ipynb
"""
client_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxOTQ2MywidG9rZW5faWQiOjQwNzJ9.MsF_ZqRrFDRikisVrfD-8BWNwF60RGrWEXrBWjSrnjk"
model_of_choice = "luminous-base"

from aleph_alpha_client import Client, Prompt, SemanticEmbeddingRequest, SemanticRepresentation
from typing import Sequence
import math
import numpy as np

client = Client(client_token)

# the helper function to embed text
def embed(text: str, representation: SemanticRepresentation):
    request = SemanticEmbeddingRequest(prompt=Prompt(text), representation=representation)
    result = client.semantic_embed(request, model = model_of_choice)
    return result.embedding

# the helper function to compute cosine similarity
def cosine_similarity(a: Sequence[float], b: Sequence[float]) -> float:
    dot_product = sum(x * y for x, y in zip(a, b))
    magnitude_a = math.sqrt(sum(x * x for x in a))
    magnitude_b = math.sqrt(sum(x * x for x in b))
    return dot_product / (magnitude_a * magnitude_b)

# the helper function to print the similarity between the query and text embeddings
def print_results(texts, query, query_embedding, text_embedding):
    for i, text in enumerate(texts):
        similarity = round(cosine_similarity(query_embedding, text_embedding[i]), 3)
        print(f"Similarity between {query} and {text}: {similarity}")

# print( np.argmax(np.array([[1.6, 1.8, 1.5], [1,2,3], [100,20,300]], float), axis=1 ) )  ???
        
texts = ["Nodular melanoma",
         "Superficial spreading melanoma",
         "Lentigo maligna melanoma"]

query = "What are the main types of melanoma?"

symmetric_query_embedding = embed(query, SemanticRepresentation.Symmetric)
asymmetric_query_embedding = embed(query, SemanticRepresentation.Query)
symmetric_text_embeddings = [embed(text, SemanticRepresentation.Symmetric) for text in texts]
asymmetric_text_embeddings = [embed(text, SemanticRepresentation.Document) for text in texts]

# print("\nSymmetric semantic search: ")
# # print_results( texts, query, symmetric_query_embedding, symmetric_text_embeddings)
# print("\nAsymmetric semantic search: ")
# print_results( texts, query, asymmetric_query_embedding, asymmetric_text_embeddings)

query_long = "What are the different types of search engines?"
text_long = """There are seven types of search engines: general, vertical, hybrid, metasearch, web search, image search, and video search engines. 
General Search Engines: A general-purpose search engine is a search engine that indexes and ranks web pages based on their content for a wide range of topics. 
The most popular general-purpose search engines are Google, Yahoo, and Bing. 
Vertical Search Engine: A vertical search engine is a search engine that specializes in a particular type of content. 
Vertical search engines are often used to find specific types of information, such as images, videos, news, or product reviews. 
Some popular vertical search engines include Google Images, YouTube, and Amazon. 
Hybrid Search Engine: A hybrid search engine is a search engine that uses more than one search algorithm to find results. This means that the search engine can use different techniques to find the best results for a query. 
Meta Search Engine: A meta search engine is a search engine that aggregates results from multiple other search engines and presents them to the user in a single list. Metasearch engines are often used to compare results from different general-purpose or vertical search engines. 
Some popular metasearch engines include Dogpile and MetaCrawler. Web Search Engines: Web search engines are the most common type of search engine. They allow users to search for websites by keyword or phrase. The results of a web search are typically a list of websites that match the user’s query. 
Image Search Engines: Image search engines allow users to search for images by keyword or phrase. The results of an image search are typically a list of images that match the user’s query. 
Video Search Engines: Video search engines allow users to search for videos by keyword or phrase. The results of a video search are typically a list of videos that match the user’s query."""

text_chunks = text_long.split("\n")
long_text_embeddings = [embed(text, SemanticRepresentation.Document) for text in text_chunks]
long_query_embedding = embed(query_long, SemanticRepresentation.Query)
top_index = np.argmax([cosine_similarity(long_query_embedding, embedding) for embedding in long_text_embeddings])

print(f"The most similar chunk is at the index {top_index}: {text_chunks[top_index]}")
print(f"The similarity is {cosine_similarity(long_query_embedding, long_text_embeddings[top_index])}:.3f")




