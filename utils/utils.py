import os
from googlesearch import search
from bs4 import BeautifulSoup
def get_prompt(filename):
    """
    reads a prompt from a file and returns it

    parameters:
    filename (str): filename of the prompt

    returns:
    str: the prompt
    """
    prompts_dir = os.path.join(parent_dir, 'prompts')
    file_path = os.path.join(prompts_dir, filename)
    with open(file_path, 'r') as file:
        prompt = file.read()
    
    return prompt

def search_google(query,num_results=10, lang="en",advanced=True):
    """
    find links on google 

    parameters:
    query (str): search query , num_results (int) : number of results, lang (str) : language, advanced (bool) : advanced search

    returns:
    list of links
    """
    return search(query, num_results=num_results, lang=lang,advanced= advanced)


def extract_text_from_website(url):
    """
    Extract the text content from a given URL
    
    Parameters:
    url (str): The URL of the webpage from which to extract the text.
    
    Returns:
    str: The extracted text content of the webpage.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
    }
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.content, "lxml")

    for script in soup(["script", "style"]):
        script.extract()  

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = "\n".join(chunk for chunk in chunks if chunk)

    return text

