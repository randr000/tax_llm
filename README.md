# Tax RAG App - Chat Service

### This service is used to create the vector store of [Publication 17](https://www.irs.gov/pub/irs-pdf/p17.pdf) and runs the chatbot.

## How to Run Locally

Make sure [Python](https://www.python.org/downloads/) is installed.

Create a Python virtual environment from the project's root directory:
```bash
python3 -m venv env
```
Activate the Python virtual environment:
```bash
source env/bin/activate
```
Install dependencies:
```bash
pip install requirements.txt
```

You then need a vector database. You can use Qdrant. Here are the [instructions](https://qdrant.tech/documentation/guides/installation/#docker) to install locally using Docker.

Copy sample.env:
```bash
cp sample.env .env
```
Add environment variable values to .env file:
```
QDRANT_API_KEY=<can leave blank if running locally. Obtain API key from Qdrant if hosting vector store with them>
QDRANT_HOST=http://localhost:6333
QDRANT_COLLECTION_NAME=<Name of vector store collection, can be whatever you like>
PDF_FILE_NAME=<Name of PDF file of source document, can leave blank if no PDF>
TXT_FILE_NAME=<Name of >
HUGGINGFACEHUB_API_TOKEN=<Obtain API key from https://huggingface.co/>
UVICORN_HOST=<IP address to bind to uvicorn socket, default: 127.0.0.1>
UVICORN_PORT=<Port to bind to uvicorn socket, default: 8000>
```
Create a Qdrant collection. Before running the command, make sure your Qdrant Docker container is running.
```bash
python create_collection.py
```
The next step would be to create a vector store using your own data. Your data must be in a text file. If it is in a pdf file, please run the following from the command line first.
```bash
python pdf_to_txt.py
```
The names of the pdf and text file will match the names specified in the .env file.

Create vector store embeddings:
```bash
python create_vector_store
```
To create the embeddings, this app uses the following embeddings model from Hugging Face:
[hkunlp/instructor-xl](https://huggingface.co/hkunlp/instructor-xl)

Once the vector embeddings have been created, it is time to run the app. The app uses the following LLM model from Hugging Face: [mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)

To run the chatbot directly in the terminal:
```bash
python chat.py
```

To run the back-end API service:
```bash
python app.py
```
It is recommended to run the back-end API service within a Docker container. The Dockerfile located in the project's root directly can be used to create the image.

## Front-End Links
[Front-End Site Live](https://taxragapp.vercel.app/)<br>
[Front-End Site README](https://github.com/randr000/tax_llm_next_app)