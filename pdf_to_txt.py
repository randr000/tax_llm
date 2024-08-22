from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os

load_dotenv()
PDF_FILE_NAME=os.getenv('PDF_FILE_NAME')
TXT_FILE_NAME=os.getenv('TXT_FILE_NAME')

def get_pdf_text(pdf):
    text = ''
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

if __name__ == "__main__":
    with open(PDF_FILE_NAME, 'rb') as pdf:
        text = get_pdf_text(pdf)
    with open(TXT_FILE_NAME, 'w') as txt:
        txt.write(text)