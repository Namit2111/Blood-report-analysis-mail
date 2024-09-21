# Project Name

## Setup Instructions

To get started with the project, follow these steps:

1. **Set Up a Virtual Environment**  
   Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

2. **Install Requirements**  
   Install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**  
   Start the application:
   ```bash
   python main.py
   ```

## Folder Structure

- **agents/**: Contains all CrewAI agents.
- **app/**: Contains Flask routes for the application.
- **tasks/**: Contains all CrewAI tasks.
- **tools/**: Contains tools used by the agents.
- **utils/**: Contains utility functions to help with various tasks.

## Environment Variables

You will need to set the following environment variables in a `.env` file:

```plaintext
GEMINI_API_KEY = ""
MODEL = ""  #gemini/gemini-1.5-flash used by me
USER = ""
PASSWORD = ""
```

## Example Usage

A sample script `sample_use_api.py` is included to demonstrate how to use the routes correctly. Refer to this file for guidance on making requests to the API.
