# industry_llm
工业大模型：
- 预训练 industry-base
- 微调 industry-chat
- 基于大模型和知识库的工业大模型: langchain ✅
- Agent工业大模型：调用每日数据，进行数据分析
- 多模态工业大模型：用于识别工业流程上的缺陷检测、安全帽正确佩戴等场景

## Getting started
data_extract：function api
- 抽取日报数据，为之后的Agent提供数据支持：✅
- 将数据进行数据表存储，提供在线接口查询功能：✅
- 赋予LLM的接口调用能力，实现工业数据分析

backend
- 后端api数据调用：python main.py
- 数据接口：✅
- 数据表存储：✅
- 数据表查询：✅

