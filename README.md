# MedBot
Medical response machine.

│
├── backend
│   ├── __init__.py              # 初始化文件
│   ├── main.py                  # API服务的主文件
│   ├── models
│   │   ├── __init__.py
│   │   └── medbot.py     # 加载和管理医疗模型
│   ├── gpt
│   │   ├── __init__.py
│   │   └── gpt_model.py         # 加载和管理GPT模型
│   ├── routes
│   │   ├── __init__.py
│   │   └── ask.py               # 处理问答请求的路由
│   ├── security
│   │   ├── __init__.py
│   │   └── auth.py              # 实现安全和权限控制
│   ├── utils
│   │   ├── __init__.py
│   │   └── preprocess.py        # 数据预处理
│   ├── logs
│   │   ├── __init__.py
│   │   └── logger.py            # 日志记录
│   ├── config.py                # 配置文件
│   ├── requirements.txt         # API服务的依赖包
│   └── run.py                   # 启动脚本
│
├── frontend
│   ├── index.html               # 前端主页面
│   ├── styles.css               # 前端样式
│   └── script.js                # 前端逻辑
│
├── README.md                    # 项目说明文档
└── .gitignore                   # Git忽略文件