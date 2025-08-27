# How to Create Your Own Search Agent Using LangChain 

When you ask ChatGPT or other AI models something like **“What’s the latest news?”**, they often reply with outdated information.  
Why? Because most language models are trained on past data and **don’t have real-time internet access**.

That’s where **LangChain agents** + **search tools** come in.  

In this tutorial, we’ll build a **search-powered conversational agent** that can:
- Use an LLM for reasoning
- Fetch **real-time web data** (via DuckDuckGo search)
- Remember the context of the conversation

Think of it as your **personal AI assistant with live web access**. 🔥

## Why Use a Search Agent?

Here are some real-world use cases:

- **Latest news & trends** → “What’s happening in AI research today?”
- **Market/Stock updates** → “What’s the current price of Tesla stock?”
- **Research assistant** → “Find me recent articles on climate change policies.”
- **Productivity tools** → A chatbot that pulls fresh answers instead of relying only on training data.

In short, this bridges the gap between **static AI knowledge** and the **dynamic internet**.

## Prerequisites

Before starting, make sure you have:

- Python 3.9+
- An [OpenRouter](https://openrouter.ai) API key (free/paid options available)
- Installed dependencies:
  
```bash
pip install langchain langchain-openai langchain-community duckduckgo-search
````

## Step 1: Import Required Libraries

We’ll need LangChain’s LLM wrapper, a search tool, and agent utilities.

```python
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
from langchain.agents.agent_types import AgentType
from langchain.agents import initialize_agent
```

## Step 2: Initialize the LLM (via OpenRouter)

Here we use the **DeepSeek model** served via OpenRouter.
You can swap this with `gpt-4`, `gpt-3.5-turbo`, or other supported models.

```python
llm = ChatOpenAI(
    model="deepseek/deepseek-chat-v3-0324:free",
    base_url="https://openrouter.ai/api/v1",
    api_key="your_openrouter_api_key_here",
)
```

 **Why OpenRouter?**

* It supports **multiple models** (DeepSeek, Mistral, GPT, etc.)
* You don’t have to lock into one vendor
* Some models are free!

## Step 3: Add a Search Tool

To fetch live results, we’ll use **DuckDuckGoSearchRun**.

```python
search = DuckDuckGoSearchRun()

tool = [
    Tool(
        name="search",
        func=search.run,
        description="When you want real time data use this",
    )
]
```

**Why DuckDuckGo?**

* It’s lightweight and privacy-friendly
* Works well for quick factual lookups
* No API key required 

## Step 4: Add Memory (for Conversations)

Without memory, the agent forgets past messages.
We’ll use `ConversationBufferMemory` so it can keep context.

```python
memory = ConversationBufferMemory(memory_key="chat_history")
```

## Step 5: Initialize the Agent

Now, we combine everything into a conversational agent.

```python
agent = initialize_agent(
    llm=llm,
    tools=tool,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
    handle_parsing_errors=True
)
```

## Step 6: Run the Agent 🎉

Finally, let’s test it out!

```python
def webSearchAgent(question):
    result = agent.run(question)
    print(f"Agent:\n\n {result}")

webSearchAgent("Give me the latest news")
```

## Example Run

![Execution_result1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/j00ypwqs00qf2tuug5jh.png)
![Execution_result1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/12ojs9zf1qwz2lax5k0i.png)

## Final Thoughts

We just built a **real-time AI search assistant** using LangChain!
This approach is powerful because it combines:

* **Reasoning power of LLMs**
* **Real-time knowledge via search**
* **Conversation memory**

With just \~40 lines of code, you’ve got the foundation for an **AI research assistant, news bot, or productivity tool**.

💡 Did you find this useful?
Drop a ❤️ on this post and share your version of the agent in the comments. also follow me

Happy coding 


