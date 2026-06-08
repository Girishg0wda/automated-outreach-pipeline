from dotenv import load_dotenv
import os

load_dotenv()

PROSPEO_API_KEY = os.getenv("PROSPEO_API_KEY")
BREVO_API_KEY = os.getenv("BREVO_API_KEY")