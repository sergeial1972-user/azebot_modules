class Section:
    def __init__(self, role, prompt):
        role: str
        prompt: str






class PromptBuilder:
    def __init__(self):
        self.final_prompt = []

    async def add_section(self, section: Section):
        section_dict = {
            "role": section.role,
            "prompt": section.prompt,
        }

        self.final_prompt.append(section_dict)

    async def get_final_prompt(self):
        return self.final_prompt


