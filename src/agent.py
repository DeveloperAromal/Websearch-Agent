from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
from langchain.agents.agent_types import AgentType
from langchain.agents import initialize_agent

from dotenv import load_dotenv
import os


load_dotenv()

def webSearchAgent(question):

    llm = ChatOpenAI(
        model = "deepseek/deepseek-chat-v3-0324:free",
        base_url = "https://openrouter.ai/api/v1",
        api_key = os.getenv("OPENROUTER_API_KEY"),
    )
    
    search = DuckDuckGoSearchRun()

    tool = [
        Tool  (
            name = "search",
            func = search.run,
            description = "When you want real time data use this",
        )
    ]
    
    memory = ConversationBufferMemory(memory_key = "chat_history")
    
    agent = initialize_agent(
        llm = llm,
        tools = tool,
        agent = AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory = memory, 
        verbose = True,
        handle_parsing_errors = True
    )
    
    result = agent.run(question)
    print(f"Agent:\n\n {result}")
    
webSearchAgent("Give me some latest news about Ai")
