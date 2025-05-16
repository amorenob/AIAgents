import os

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# Define the directory containing the text file and the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "books", "odyssey.txt")
persistent_dir = os.path.join(current_dir, "db", "chroma_db")

# check if the Chroma vector store already exist
if not os.path.exists(persistent_dir):
    print("Persistent directory does not exist. Initializing vector db")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"The file {file_path} does not exist. Please check the path."
        )
    
    loader = TextLoader(file_path)
    documents = loader.load()
    
    # Split the documento into chunks
    text_spliter = CharacterTextSplitter(chunk_size=1000, chunk_overlap = 100)
    docs = text_spliter.split_documents(documents)
    
    # Display information about the slpit documents
    print("\n --- Document Chunks Information ---")
    print(f"Number of documents chunks : {len(docs)}")
    print(f"Sample chunk: \n {docs[0].page_content}\n")

    # create embedding
    print("\n --- creating Embedings --- \n")
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    print("\n --- Finished creating Embedings --- \n")
    
    print("\n --- Creating vector store--- \n")
    db = Chroma.from_documents(docs, embeddings, persist_directory=persistent_dir)
    print("\n --- Finished creating vector store--- \n")

else:
    print("Vector store already exist")