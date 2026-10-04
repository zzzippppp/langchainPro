import os
from typing import Optional
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from scripts.regsetup import description
from langgraph.checkpoint.memory import InMemorySaver

# 读取.env配置文件中的相关信息
load_dotenv(override=True)

DB_URL = os.getenv("DATABASE_URL")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASEURL = os.getenv("DEEPSEEK_BASEURL")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

web_search = TavilySearch(
    api_key=TAVILY_API_KEY,
    max_results=2
)

checkpointer = InMemorySaver()

config = {
    "configurable":{
        "thread_id":"1"
    }
}

llm = ChatDeepSeek(
    model="deepseek-flash",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASEURL,
    extra_body={"thinking": {"type": "disabled"}}
)

@tool
def get_weather(city:str)->str:
    '''
    获取指定城市的天气

    Args:
        city:城市名称
    '''
    return f"{city}今天的天气是晴天"


agent = create_agent(llm,tools=[get_weather,web_search],checkpointer=checkpointer)

while True:
    req = input()
    resp = agent.invoke({"messages":[HumanMessage(req)]},config = config)
    print(resp["messages"][-1].content)

