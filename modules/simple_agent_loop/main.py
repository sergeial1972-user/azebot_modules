#imports
from prompt_builder import Section, PromptBuilder

def main(user_prompt):
    max_steps = 10

    prompt_builder = PromptBuilder()

    system_prompt = Section(role="system", prompt="you are helpful assistant")
    prompt_builder.add_section(system_prompt)

    user_prompt = Section(role = "user", prompt = user_prompt)
    prompt_builder.add_section(user_prompt)

    final_prompt = prompt_builder.final_prompt









    i = 0
    while i < max_steps:



