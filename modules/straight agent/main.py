#imports
import os
import sys
from llm_handler import LLMHandler


_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
if _MODULE_DIR not in sys.path:
    sys.path.insert(0, _MODULE_DIR)

from prompt_builder import Section, PromptBuilder
from llm_handler import LLMHandler

async def main(user_prompt):
    llm = LLMHandler()
    max_steps = 10

    prompt_builder = PromptBuilder()

    system_prompt = Section(role="system", content="you are helpful assistant")
    await prompt_builder.add_section(system_prompt)

    user_prompt = Section(role = "user", content = user_prompt)
    await prompt_builder.add_section(user_prompt)

    final_prompt = prompt_builder.final_prompt

    result = await llm.call_llm(final_prompt)

    return result