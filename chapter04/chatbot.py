import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
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

messages = []
messages.append(SystemMessage("你是DeepseekAI，很善于回答问题"))
response = ""


while True:
    req = input("问些什么：\n")
    if req == "quit":
        print("欢迎下次再见")
        break
    messages.append(HumanMessage(req))
    for chunk in llm.stream(messages):
        print(chunk.text,end="",flush=True)
        response += chunk.text

    messages.append(AIMessage(response))
