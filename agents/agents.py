from crewai import Agent
from tools.internet_search import search_google,extract_text_from_website
from tools.email import send_email
from config.config import model ,max_iter
# Gemine Agent
# =============
# Extract relevant information from a medical report PDF and return it in a structured JSON format.
gemini_agent = Agent(
   role="You are an AI assistant specialized in extracting and structuring data from medical PDF reports.",
    goal="Extract relevant information from a medical report PDF and return it in a structured JSON format.",
    backstory="An AI assistant powered by Google's advanced language model. You specialize in extracting medical data from PDF files and organizing it into a structured format.",
    llm=model,
    verbose=False,
    max_iter = max_iter
)

# Google Query Agent
# =================
# Create google queries from a medical report PDF
google_query_agent = Agent(
    role="You are an AI agent you specialize in creating google searchable queries",
    goal="Create google queries from a medical report PDF",
    backstory="An AI assistant powered by Google's advanced language model. You specialize in creating google queries from medical data.",
    llm=model,
    verbose=False,
    max_iter = max_iter
)

# Query Review Agent
# ==================
# Review and analyze and create a better google querie
query_review = Agent(
    role="You are an AI agent you specialize in reviewing and creating better google queries",
    goal="Review and analyze and create a better google querie",
    backstory="An AI assistant powered by Google's advanced language model. You specialize in reviewing and analyzing and creating google queries.",
    llm=model,
    verbose=False,
    max_iter = max_iter
)

# Best Article Agent
# =================
# Find the best article for a given query and keywords
best_article_agent = Agent(
    role="You are an AI agent you specialize in finding the best article for a given query and keywords",
    goal="Find the best article for a given query and keywords",
    backstory="An AI assistant powered by Google's advanced language model. You specialize in finding the best article for a given query and keywords.",
    llm=model,
    verbose=False,
    max_iter = max_iter,
    tools=[search_google]
)

# Answer Agent
# ===========
# Extract text from websites and find best answers in them
answer_agent = Agent(
    role="You are an AI agent you specialize in extracting text from websites and find best answers in them",
    goal="Extract text from websites and find best answers in them",
    backstory="An AI assistant powered by Google's advanced language model. You specialize in extracting text from websites and find best answers in them.",
    llm=model,
    verbose=False,
    max_iter = max_iter,
    tools=[extract_text_from_website]
)

# Email Agent
# ==========
# Create and send emails
email_agent = Agent(
    role="You are an AI agent you specialize in creating and sending emails",
    goal="Create and send emails",
    backstory="An AI assistant powered by Google's advanced language model. You specialize in creating and sending emails.",
    llm="gemini/gemini-1.5-flash",
    verbose=False,
    max_iter = max_iter,
    tools=[send_email]
)
