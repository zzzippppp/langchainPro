import os
import time
from dotenv import load_dotenv
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

messages = [
    {"role":"system","content":"你是一个专业的python老师,善于用小学生都听得懂的语言回复问题"},
    {"role":"user","content":"帮我解释一下装饰器"}
]
start = time.perf_counter()
for chunk in llm.stream(messages):
    print(chunk.text,end="",flush=True)
elapsed = time.perf_counter() - start
print(f"耗时: {elapsed:.2f} 秒")
