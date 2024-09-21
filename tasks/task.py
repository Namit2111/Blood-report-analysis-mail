from crewai import Task
from agents.agents import gemini_agent, google_query_agent, query_review, best_article_agent, answer_agent, email_agent
# Task 1: Extract relevant information from a medical report PDF and return it in a structured JSON format
extract_patient_data_task = Task(
    expected_output="Return the relevant structured data in JSON format(contains all relevant info and patient name and age and gender) from the blood test report PDF data  {data}.",
    description=(
        "1. You are given raw txt of a real blood report of a real patient it includes patient name, test results and other relevant information too.\n"
        "2. Read through the extracted text and identify key details such as patient name, test results, and other relevant information. Only use the exact data that is present in the text\n"
        "3. For each test result, determine if the value is high or low compared to normal ranges.\n"
        "4. Return a structured JSON format that includes only the test results that are outside the normal range, "
        "along with a label indicating whether each result is 'high' or 'low'."
    ),
    agent = gemini_agent
)

# Task 2: create a google queries for the medical report so that the problem of the patient can be searched on google easily
create_google_query_task = Task(
    expected_output="return  patient name a single google querie and relevant keywords to the query in a JSON format.",
    description=(
        "1.you are given a json format values of a patient medical report. create a google queries for the medical report so that the problem of the patient can be searched on google easily \n"
        "2.Return a single google querie and relevant keywords to the query in a JSON format."
    ),
    agent = google_query_agent,
    context=[extract_patient_data_task]
)

# Task 3: review and analyze the google queries and keywords and make it small and efficient.
review_google_query = Task(
    expected_output="A single json file with patient_name and query and relevant keywords list only.",
    description=(
        "1. you are given a google querie for the medical report. review and analyze the google queries and keywords and make it small and efficient. \n"
        "2. final query should not be big , should be in format query,keywords,patient_name. should be small\n"
        "3.Make sure it is google search compatible."
    ),
    agent = query_review,
    context = [create_google_query_task]
)

# Task 4: find related articles for the query and relevant keywords and find best result in those link and thier description
find_related_articles = Task(
    expected_output = "return a json with a list of top 3 links and patient_name, query,keywords",
    description = (
        "1. you are given a google querie and relevant keywords for the medical report.  \n"
        "2. find related articles for the query and relevant keywords. you can use the search_google(it takes a single string as input, try to keep input plain with no slashes) tool it will return a dict of urls and their corresponding descriptions as strings.\n"
        "3. you can use the tool only once if tool gives unexpected output then you can use it again , expected out is a dict of urls and their corresponding descriptions s.\n"
        "4. find best result in those link and thier description find top 3 links that are relevant to the query and relevant keywords. \n"
        "5. return those 3 top links with patient name, query,keywords"
    ),
    agent = best_article_agent,
    context = [review_google_query]
)

# Task 5: use the tool extract_text_from_website(takes list of links as input) to extract text from all the links and find best answer in the extracted text related to the query and relevant keywords and prepare a cure for the patient based on the best answer
find_cure = Task(
    expected_output = "return a json with query,keywords,patient_name,cure",
    description = (
        "1. you can use the tools to extarct data from a list of links. \n"
        "2. but you can use the tool only once if tool gives unexpected output then you can use it again , expected out is text as string of web pages.\n"
        "2. find best answer in the extracted text related to the query and relevant keywords. \n"
        "3.prepare a cure for the patient based on the best answer."
        "3. return json of query,keywords,patient_name,cure"
    ),
    agent = answer_agent,
    context = [find_related_articles]
)

# Task 6: create an email based on the query,keywords,patient_name,cure and send the patient to {email} using send_email tool
send_email_task = Task(
    expected_output = "return a json with email based on the query,keywords,patient_name,cure",
    description = (
        "1. create an email based on the query,keywords,patient_name,cure to send the patient\n "
        "2. send the email to {email} using send_email tool"
        "3. use the tool only once if tool gives unexpected output then you can use it again , expected out is a text string saying email sent\n"
    ),
    agent = email_agent,
    context = [find_cure]
)

