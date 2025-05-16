import os

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# Define the directory containing the text file and the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "books", "odyssey.txt")
persistent_dir = os.path.join(current_dir, "db", "chroma_db")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

db = Chroma(persist_directory=persistent_dir, embedding_function=embeddings)

query = "Who is Odysseus wife?"

retriever = db.as_retriever(
    search_type = "similarity_score_threshold",
    search_kwargs={"k": 3, "score_threshold": 0.4}
)

relevant_docs = retriever.invoke(query)

print("\n --- Relevant documents --- \n")

for i, docs in enumerate(relevant_docs, 1):
    print(f"Document {i} \n {docs.page_content}\n")
    if docs.metadata:
        print(f"Source: {docs.metadata.get('source', 'Unknown')}\n")
    