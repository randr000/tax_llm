from dotenv import load_dotenv
import qdrant_client
import os
import qdrant_client.models

load_dotenv()
QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')
QDRANT_HOST = f"{os.getenv('QDRANT_HOST')}/"
QDRANT_COLLECTION_NAME = os.getenv('QDRANT_COLLECTION_NAME')

# create a qdrant client

client = qdrant_client.QdrantClient(
    url=QDRANT_HOST,
    api_key=QDRANT_API_KEY
)

# create collection
client.create_collection(
    collection_name=QDRANT_COLLECTION_NAME,
    vectors_config=qdrant_client.models.VectorParams(size=768, distance=qdrant_client.models.Distance.COSINE)
)