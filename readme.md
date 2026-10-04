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

## Day04
1. Agent的创建与调用
2. Tavily工具的使用

## Day05
1. Function calling，即HUMANMESSAGE -> AIMESSAGE -> TOOLMESSAGE -> AIMESSAGE 属于langchain的内容
2. REACT 是FUNCTION calling的加强版，进行思考-行动-观察的循环，直到输出不再调用工具为止 属于langgraph的内容
3. 可以设置重试次数
4. 为Agent设置名称，可以加强管理，加强审计，方便调用
5. 可以为agent设置系统提示词
6. Agent结构化输出 ToolStrategy ProviderStrategy源头厂商内置
7. 为Agent设置流式输出
8. 中间件：即钩子函数，在生命周期中进行一些横向的操作，属于控制反转的体现
9. langchain自带中间件大致分为六类：
   1. 成本控制与资源控制类
   2. 稳定性与容错保障类
   3. 安全与合规风控类
   4. 决策增强与智能编排类
   5. 执行能力扩展类
   6. 开发调试与测试辅助类
10. 常用的几个中间件：
    1. SummarizationMiddleware中间件，对历史消息列表进行 摘要&总结 ，达到 压缩上下文 的效果。在 达到触发条件 时，调用大模型对历史消息进行摘要， 将摘要的结果作为HumanMessage，放到消息列表最开始的位置。
    2. HumanInTheLoopMiddleware中间件，HumanInTheLoopMiddleware（人在环中间件、人工审核中间件）在 工具调用前 中断Agent运行，等待用户对工具调用请求决策。
    3. PIIMiddleware中间件，PII中间件用于检测和处理对话中的个人身份信息（Personally Identifiable Information，PII），支持自定义处理策略。
    4. TodoListMiddleware中间件，TodoListMiddleware中间件赋予了Agent 任务规划 和 追踪进度 的能力，可以 应对复杂的多步任务，TodoListMiddleware 中间件强制它把计划挂在全局状态里，时刻提醒它“下一步该干什么”。

## Day06
1. 短期记忆不跨会话（state），只在会话内发挥作用，一般为上下文，可用InMemorySaver()存储，也可以用postgresql长期保存
2. 长期记忆可跨会话（store），一般保存用户偏好和用户画像类的内容

## Day07
1. RAG