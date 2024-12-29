#create prompt using templates

def create_summary_prompt(text):
    prompt_template = "Summarize the following text: {text}"
    return prompt_template.format(text=text)

# Example of using the template
input_text = "AI is rapidly changing the way we work, communicate, and solve problems."
summary_prompt = create_summary_prompt(input_text)
print("Generated Summary Prompt:", summary_prompt)
