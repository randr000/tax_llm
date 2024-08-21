from langchain_community.document_loaders import UnstructuredPDFLoader

local_path = 'p17.pdf'

if local_path:
    loader = UnstructuredPDFLoader(file_path=local_path)
    data = loader.load()
else:
    print('Upload a PDF file')

print(data[0].page_content)