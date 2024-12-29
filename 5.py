#5. Generating Multiple Prompts Dynamically Using Lists and Strings

def generate_prompts_from_data(data_list):
    prompts = []
    for item in data_list:
        prompt = f"Explain {item} in simple terms."
        prompts.append(prompt)
    return prompts

# Sample data list (e.g., topics to explain)
data_list = ["quantum computing", "machine learning", "climate change"]

# Generate prompts
prompts = generate_prompts_from_data(data_list)

# Print each prompt
for prompt in prompts:
    print(prompt)
