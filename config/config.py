from dotenv import load_dotenv
import os
load_dotenv()

max_iter = 3
model = os.getenv("MODEL")
a_user = os.getenv("USER")
a_password = os.getenv("PASSWORD")