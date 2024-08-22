from langchain_qdrant import QdrantVectorStore
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
import os

load_dotenv()
QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')
QDRANT_HOST = f"{os.getenv('QDRANT_HOST')}/"
QDRANT_COLLECTION_NAME = os.getenv('QDRANT_COLLECTION_NAME')

embeddings = HuggingFaceInstructEmbeddings(model_name='hkunlp/instructor-xl')

# create vector store

vector_store = QdrantVectorStore.from_existing_collection(
    embeddings=embeddings,
    collection_name=QDRANT_COLLECTION_NAME,
    url=QDRANT_HOST,
    api_key=QDRANT_API_KEY
)

def get_chucks(text):
    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    chunks = text_splitter.split_text(text)
    return chunks