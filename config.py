from dotenv import load_dotenv,dotenv_values
import os

# Load environment variables
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
