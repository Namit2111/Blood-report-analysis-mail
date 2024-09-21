from langchain.tools import tool
import PyPDF2
import re
import json
@tool("Tool to extract text from a pdf file")
def extract_pdf(pdf_file):
    """
    Tool to extract text from a pdf file
    
    Parameters:
    pdf_file (Path): path to the pdf file
    
    Returns:
    str: the extracted text from the pdf
    """
    reader = PyPDF2.PdfReader(pdf_file)
    pdf_data = ""
    for page_num in range(len(reader.pages)):  # Corrected the range statement
        pdf_data += reader.pages[page_num].extract_text() or ""  # Correct way to access the page
    
    return pdf_data

# @tool("Tool to organize extracted text into structured JSON format")
# def organize_into_json(text):
#     """
#     Organizes extracted text json into structured JSON format.
    
#     Parameters:
#     text (str): The extracted text json from the PDF file.
    
#     Returns:
#     dict: Structured data extracted from the text.
#     """
#     structured_data = json.loads(text)
#     return structured_data

