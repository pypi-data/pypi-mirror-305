# from langchain.document_loaders import DirectoryLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
# from langchain.embeddings import OpenAIEmbeddings
import chromadb.utils.embedding_functions as embedding_functions
from langchain_community.vectorstores import Chroma
import openai
import chromadb
import os
import shutil
import ollama
# openai.api_key = "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"

# openai.OpenAI(
#   base_url = "https://integrate.api.nvidia.com/v1",
#   api_key = "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",
# )

# openai_client.api_key


CHROMA_PATH = "chroma"
DATA_PATH = "../documents"


client = chromadb.Client()
collection = client.create_collection(name="docs")



def generate_data_store(prompt: str):
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)
    data = retrieve_data(prompt)
    # generate_response(data, prompt)



def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents


def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    return chunks

def clear_database()-> None:
    # Clear out the database first.
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)


def save_to_chroma(chunks: list[Document]):
    clear_database()
   # store each document in a vector embedding database
    for document_index, document in enumerate(chunks):
        document_content = document.page_content
        document_id = str(document_index)
        embedded_data = ollama.embeddings(model="mxbai-embed-large", prompt=document_content)
        embedding = embedded_data["embedding"]
        collection.add(
            ids=[document_id],
            embeddings=[embedding],
            documents=[document_content]
        )
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")
    
def retrieve_data(prompt):
    # generate an embedding for the prompt and retrieve the most relevant doc
    response = ollama.embeddings(
    prompt=prompt,
    model="mxbai-embed-large"
    )
    
    results = collection.query(
    query_embeddings=[response["embedding"]],
    n_results=1
    )
    data = results['documents']
    print(data)
    return data

def generate_response(data, prompt):
    # generate a response combining the prompt and data we retrieved in step 2
    output = ollama.generate(
    model="llama2",
    prompt=f"Using this data: {data}. Respond to this prompt: {prompt}"
    )

    print(output['response'])


generate_data_store("How many class methods in this project?")
