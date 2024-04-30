import os

class Config:
    API_TOKEN = os.getenv("API_TOKEN", "your_default_token_here")
    # Add more configuration variables as needed
