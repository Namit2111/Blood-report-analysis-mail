from langchain.tools import tool
# from utils.utils import search_google,calculate_keyword_weights,rate_text_based_on_keywords,extract_text_from_website
from googlesearch import search
from bs4 import BeautifulSoup
import requests
@tool("This is helpful to get search results from google")
def search_google(query):
    """
    Get search results from Google.

    Parameters:
    query (str): The search query to search on Google.

    Returns:
    dict: A dictionary of URLs and their corresponding descriptions as strings.
    """
    final_dict = {}
    results = search(query, num_results=10, lang="en", advanced= True)
    for result in results:
        if result.url.endswith(".pdf"):
            continue
        
        final_dict[result.url] = result.description
    return final_dict




@tool("This is helpful to extract text from a website links ")
def extract_text_from_website(urls):
    """
    Extract the text content from a given list of URLs
    
    Parameters:
    urls (list): The list of URLs of the webpages from which to extract the text.
    
    Returns:
    str: The extracted text content of the webpage.
    """
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
    }
    final_text = ""
    for url in urls:
        r = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(r.content, "lxml")

        for script in soup(["script", "style"]):
            script.extract()  

        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = "\n".join(chunk for chunk in chunks if chunk)
        final_text += text
    return final_text

if __name__ == "__main__":
    print(search_google("hello world"))