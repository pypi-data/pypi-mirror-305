import simplemind as sm

print(
    sm.generate_text(
        prompt="Hello, world!", llm_provider="groq", llm_model="llama3-8b-8192"
    )
)
