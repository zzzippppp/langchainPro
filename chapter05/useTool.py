import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

# 读取.env配置文件中的相关信息
load_dotenv(override=True)

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASEURL = os.getenv("DEEPSEEK_BASEURL")

llm = ChatOpenAI(
    model="deepseek-flash",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASEURL,
)

@tool
def get_weather(city:str) -> str:
    """
    获取指定城市的天气信息
    """

    return "晴天"

model_tool = llm.bind_tools([get_weather])

response = model_tool.invoke("今天天气如何")

print(response.tool_calls)