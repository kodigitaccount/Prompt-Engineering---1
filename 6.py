
#6. Advanced Prompt Engineering

def create_stepwise_prompt(context):
    step1_prompt = f"Summarize this text: {context}"
    
    # Generate an AI summary (this is hypothetical code for an API)
    ai_summary = "This is a summary of the context."  # Placeholder for the actual AI API response
    
    step2_prompt = f"Based on the summary: '{ai_summary}', answer the following question: What are the key points?"
    
    return step1_prompt, step2_prompt

context = "Artificial intelligence has become a pivotal technology in the 21st century..."
step1, step2 = create_stepwise_prompt(context)

print("Step 1 Prompt:", step1)
print("Step 2 Prompt:", step2)
