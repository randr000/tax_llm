from langchain_qdrant import QdrantVectorStore
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
import os

load_dotenv()
QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')
QDRANT_HOST = f"{os.getenv('QDRANT_HOST')}/"
QDRANT_COLLECTION_NAME = os.getenv('QDRANT_COLLECTION_NAME')
TXT_FILE_NAME=os.getenv('TXT_FILE_NAME')

embeddings = HuggingFaceInstructEmbeddings(model_name='hkunlp/instructor-xl')

# create vector store

vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name=QDRANT_COLLECTION_NAME,
    url=QDRANT_HOST,
    # api_key=QDRANT_API_KEY,
)

def get_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    chunks = text_splitter.split_text(text)
    return chunks

with open(TXT_FILE_NAME, 'r') as f:
    raw_text = f.read()

texts = get_chunks(raw_text)

vector_store.add_texts(texts)