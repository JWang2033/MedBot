import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

class Config:
    # OpenAI API 配置
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # 模型相关配置
    MEDBOT_MODEL_PATH = "path/to/medbot_model"

    # 应用程序配置
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = 8000

    # 数据库配置
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

    # 其他配置
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

config = Config()
