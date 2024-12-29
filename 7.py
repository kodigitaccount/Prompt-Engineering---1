
#7. Using Prompt Templates with f-Strings

def generate_flexible_prompt(action, subject, tone):
    prompt = f"Write a {tone} {action} about {subject}."
    return prompt

# Example inputs
action = "story"
subject = "the first human on Mars"
tone = "adventurous"

# Generate prompt
prompt = generate_flexible_prompt(action, subject, tone)
print("Generated Prompt:", prompt)
