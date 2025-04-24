from dotenv import load_dotenv
import os

class EnvManager():
    def __init__(self):
        load_dotenv()

    def get_api_key():
        api_key = os.getenv("API_KEY")
        print(f"api_key: {api_key}")
        if api_key:
            return api_key
        else:
            return None

    def get_search_engine_id():
        search_engine_id = os.getenv("SEARCH_ENGINE_ID")
        print(f"search_engine_id: {search_engine_id}")
        if search_engine_id:
            return search_engine_id
        else:
            return None