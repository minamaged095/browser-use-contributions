import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from browser_use import Agent

load_dotenv()

# Initialize the model
llm = ChatOpenAI(
	model='gpt-4o',
	temperature=0.0,
)
task = """  get human help"""

agent = Agent(task=task, llm=llm)


async def main():
	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())
