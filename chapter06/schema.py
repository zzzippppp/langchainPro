import os
from typing import Optional
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from scripts.regsetup import description

# 读取.env配置文件中的相关信息
load_dotenv(override=True)

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASEURL = os.getenv("DEEPSEEK_BASEURL")

llm = ChatDeepSeek(
    model="deepseek-flash",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASEURL,
    extra_body={"thinking": {"type": "disabled"}}
)

class Weather(BaseModel):
    '''天气相关信息'''
    city:str = Field(description="城市")
    qiwen:int = Field(30,description="城市气温摄氏度")
    shjdu:Optional[int] = Field(50,description="当地湿度")

@tool
def get_weather(city:str,qiwen:int,shidu:int)->str:
    '''
    获取当地天气情况
    '''
    return f"今天{city}的气温为{qiwen}，湿度为{shidu}"

model_schema = llm.with_structured_output(Weather)
model_tool = llm.bind_tools([get_weather])
message = [HumanMessage("今天北京天气如何")]
response = model_tool.invoke("今天北京天气如何")
message.append(response)
for tool_call in response.tool_calls:
    message.append(get_weather.invoke(tool_call))
res = model_schema.invoke(message)

print(res.city,res.qiwen,res.shjdu)