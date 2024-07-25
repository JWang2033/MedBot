import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

class Config:
    # OpenAI API
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # 模型相关配置
    MEDBOT_MODEL_NAME = "allenai/biomed_roberta_base"

    # 应用程序配置
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = 8000

    # 数据库配置
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

    # 其他配置
    SECRET_KEY = os.getenv("SECRET_KEY")

config = Config()
