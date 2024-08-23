from dotenv import load_dotenv
import os
import qdrant_client
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.llms.huggingface_endpoint import HuggingFaceEndpoint

load_dotenv()
QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')
QDRANT_HOST = f"{os.getenv('QDRANT_HOST')}/"
QDRANT_COLLECTION_NAME = os.getenv('QDRANT_COLLECTION_NAME')
HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')

def get_vector_store():
    # create a qdrant client

    client = qdrant_client.QdrantClient(
        url=QDRANT_HOST,
        api_key=QDRANT_API_KEY
    )

    embeddings = HuggingFaceInstructEmbeddings(model_name='hkunlp/instructor-xl')

    # create vector store

    vector_store = QdrantVectorStore.from_existing_collection(
        embedding=embeddings,
        collection_name=QDRANT_COLLECTION_NAME,
        url=QDRANT_HOST,
        api_key=QDRANT_API_KEY,
    )

    return vector_store

qa = RetrievalQA.from_chain_type(
    llm = HuggingFaceEndpoint(
        repo_id='mistralai/Mistral-7B-Instruct-v0.2',
        max_length=128,
        temperature=0.5,
        huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
    ),
    chain_type='stuff',
    retriever=get_vector_store().as_retriever()
)

query = "I am not married and have no children. What filing status should I use?"
print(qa.run(query))