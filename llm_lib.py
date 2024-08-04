from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


llm = ChatOpenAI(temperature=0, model_name="gpt-4o",
                 openai_api_key=os.getenv("OPENAI_API_KEY"))
