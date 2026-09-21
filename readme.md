# Langchain 学习
## Day01:
1. chatOpenAI等多个调用AI大模型api方式
2. env环境配置
3. invoke参数
    1. 直接输入
    2. message做多轮对话
    3. 消息对象 SystemMessage HumanMessage
4. invoke返回值解析
5. 多种调用方式 流式stream 批量batch 异步a...
6. 使用不同模型的其他参数
7. langsmith监控，审计
8. 多轮对话优化实战，实现短期记忆功能

## Day02:
1. content/content_block 后者可以规范输入输出，完成多模态输入
2. 通过chatprompttemplate制作提示词模板，封装提示词
    1. 两种实例化方法：直接，from_message
    2. 三种使用方式：invoke（ChatPromptValue），format(str),fromat_message(消息对象)
    3. 可以预填充提示词，以提高灵活性
3. @tool装饰器可以定义工具，注意要有"""对应的描述"""，定义完后要对工具进行挂载再使用
4. convert_to_openai_tool可以展示工具详细信息
5. parse_docstring=True设置，参数不在description中
6. 可用Pydantic（arg_schema）或者jsonschema进行传参，方便结构化输出
7. 可通过choice选择需不需要调用工具，或者强制使用某个工具
8. 报错解决方案：try-catch、agent级重试、重新调用外部工具

## Day03:
1. pydantic规范化输出
2. 