import langchain
from pydantic import SecretStr

print(langchain.__version__)

# pip依赖包
# pip install -U langchain-openai
# pip install langchain

from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# 配置 DeepSeek 模型
chat = ChatOpenAI(
    model_name = "deepseek-chat",  # 模型名称，如 deepseek-chat、deepseek-coder
    openai_api_base = "https://api.deepseek.com/v1",  # DeepSeek API 基础地址
    openai_api_key = SecretStr("sk-3ec728dff63041e1a09c82b8a34328c71"),  # 替换为你的 API Key
    max_tokens = 100,
    temperature = 0.7  # 随机性参数，0-1 之间
)

# 发送消息（单轮对话）
messages = [
    SystemMessage(content="我是一位android开发工程师"),
    HumanMessage(content="介绍下Android开发书籍,只需要简单回复，100个字以内")
]

response = chat.invoke(messages)
print("输出内容：", response.content)
print("输出长度（字符数）：", len(response.content))
