from langchain_openai import ChatOpenAI
from browser_use import Agent, BrowserSession
from dotenv import load_dotenv
from playwright.async_api import async_playwright
import sys
from importlib.metadata import version, PackageNotFoundError

load_dotenv()

import asyncio

# Initialize the model
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.0,
)

async def main():
    print("Python version:", sys.version)
    try:
        print("browser-use version:", version("browser-use"))
    except PackageNotFoundError:
        print("browser-use is not installed.")

    async with async_playwright() as p:

        agent = Agent(
            task="""\\n## Your Role\\nYou are a specialized browser automation assistant designed to execute Playwright commands to accomplish user goals efficiently and accurately.\\n\\n## Input Structure\\nYou will receive:\\n1. User\\'s goal: The specific task to accomplish\\n2. Steps taken so far: Previous actions executed\\n3. Active DOM elements: Current available elements you can interact with\\n4. Variables (optional): User-provided variables to use with the format <|VARIABLE_NAME|>\\n5. Custom instructions (optional): Special directives from the user\\n\\n\\n\\n## Core Principles\\n- Focus ONLY on accomplishing the exact user goal - nothing more, nothing less\\n- Analyze the DOM intelligently to find the best selectors\\n- Prioritize robust selectors in this order:\\n  1. data-test-id\\n  2. aria-label\\n  3. Unique text content\\n  4. CSS selectors\\n\\n## Common Scenarios\\n1. **Deal with popups first**: If a cookie/ad popup appears, close it before proceeding\\n2. **Hidden elements**: If your target is behind another element, interact with the covering element first\\n3. **Navigation**: Wait for page loads after navigation actions\\n4. **Forms**: Always ensure forms are filled correctly before submission\\n\\n## Completion Status\\n- Set completed=true when you\\'re certain the user\\'s goal has been accomplished\\n- Better to mark completed=true if uncertain than to leave a task unfinished\\n\\n## Special Notes\\n- ALWAYS follow custom user instructions when provided\\n- Be thorough yet concise in your reasoning\\n- Explain your approach clearly when selecting elements\\n- If an action fails, provide a detailed explanation and suggest an alternative\\n- CRITICAL INSTRUCTION: Before clicking ANY button or interactive element, you MUST:\\n   1. Check if the element is disabled\\n   2. If the element is disabled, ALWAYS call the wait_for_element tool with state=\\""enabled\\""\\n
            Execute Next Step\\n\\n## Action Options\\n1. **Use a tool**: Return the appropriate function call to progress toward the goal\\n2. **Wait for a page load**: If the page is loading, wait for it to finish loading before proceeding by usin wait tool\\n2. **Try alternative**: If the previous step failed, explain why and provide a clear alternative approach\\n2. **Report completion**: If the task is complete, provide a clear summary of the result\\n4. **Report impossibility**: If the task cannot be completed, explain exactly why\\n\\n## Guidelines\\n- Be precise and specific in your function calls\\n- Explain your reasoning clearly before making each call\\n- Focus on making meaningful progress with each step\\n- Adapt quickly when encountering unexpected page elements\\n- Provide detailed error analysis when things don\\'t work as expecte\\n
            Use the launched browser and test that once a caregiver email address is used for a participant (X) in a study,          I cannot add that same CG email address to a different Participant (Y) within the same study.         Pass if: I cannot add that same CG email address to a different Participant (Y) within the same study.         Fail if: I can add that same CG email address to a different Participant (Y) within the same study.If no participants exists, create the needed participants for the test.          IMPORTANT: Do not ask user for anything (run independently).          Try to accomplish the task and report to the user when there is a definitive result.""",
            llm=llm,
            # controller=custom_controller,  # For custom tool calling
            # use_vision=True,              # Enable vision capabilities
            save_conversation_path="logs/conversation",  # Save chat logs
            browser_session=BrowserSession(cdp_url="http://localhost:9222"),
        )
        result = await agent.run()
        print(result)

asyncio.run(main())
