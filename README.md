# industry_llm
工业大模型：
- 预训练 industry-base
- 微调 industry-chat
- 基于大模型和知识库的工业大模型: langchain ✅
- Agent工业大模型：调用每日数据，进行数据分析 ✅
- 多模态工业大模型：用于识别工业流程上的缺陷检测、安全帽正确佩戴等场景

## Getting started
### 预训练语料与SFT语料构建
- 预训练语料从文档中提取
- SFT语料收集过程：
- - 通过前者的文档语料进行建库。
- - 调用本地chatglm的api进行ref+query回答
- - 收集此类query-answer作为SFT语料。
- - 同时，可收集多轮问答语料。

### data_extract：Excel数据提取
- 抽取日报Excel数据，转为txt格式化数据，进而存储到Mysql数据库：✅

### sql_agent nlp2sql能力
- 通过nlp2sql的能力，将用户的自然语言转为sql语句并实现sql语句执行返回结果：✅
- 可视化数据：目前采用Vanna的库 ✅

### chatglm_chat API大模型在线访问接口
- 部署ChatGLM3-6B在线接口，为后续SFT语料做准备 ✅
- 适配Langchain的ChatGLM3-6B接口，部署chat及multi-chat的api接口 ✅
- multi-chat为Vanna库服务 ✅

### 待改进部分
- 数据库在服务端进行安装部署，本地测试demo没问题
- 数据可视化有待提升
- 模型6B的nlp2sql能力有待提升

### backend
- 数据接口：✅
- 数据表存储：✅
- 数据表查询：✅

### start
main.py 启动api服务
chat_show.py 启动chat界面，展示工具调用的能力