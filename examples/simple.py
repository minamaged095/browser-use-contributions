import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from browser_use import Agent

load_dotenv()

def cli_human_help_handler(msg: str, inst: str) -> str:
    prompt = msg
    if inst:
        prompt += "\n" + inst
    prompt += "\n> "  # terminal prompt
    return input(prompt).strip()


# Initialize the model
llm = ChatOpenAI(
	model='gpt-4o',
	temperature=0.0,
)
task = 'ask for human help then Go to kayak.com and find the cheapest flight from Zurich to San Francisco on 2025-05-01'

# agent = Agent(task=task, llm=llm, allow_yield_to_human=True, human_help_callback=cli_human_help_handler)
agent = Agent(task=task, llm=llm)


async def main():
	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())
