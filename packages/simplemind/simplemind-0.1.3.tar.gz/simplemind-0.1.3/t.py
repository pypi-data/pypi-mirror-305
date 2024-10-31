import simplemind as sm

r = sm.generate_text("Hello, world!", llm_provider="ollama", llm_model="llama3.2")
print(r)
