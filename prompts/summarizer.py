# Zero-shot vs Few-shot Summarization
zero_shot = "Summarize this: AI is transforming world..."

few_shot = """
Summarize in 1 line:
Text: 'GenAI creates new content like text, image' -> Summary: GenAI creates content.
Text: 'Prompt engineering is writing good prompts' -> Summary: Prompting is key skill.
Text: 'AI is transforming world...' -> Summary:?
"""
print(few_shot)
