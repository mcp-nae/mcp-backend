import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.client import MultiServerMCPClient  
from langchain.agents import create_agent


load_dotenv()
api_key = os.getenv("API_KEY")
llm = ChatGoogleGenerativeAI(
api_key=api_key,
model="gemini-2.5-flash",
temperature=0.5,
max_tokens=2048)
