import simplemind as sm
from pydantic import BaseModel

sm.enable_logfire()

# Create session with correct model specification
claude = sm.Session(llm_provider="groq", llm_model="mixtral-8x7b-32768")


class Poem(BaseModel):
    title: str
    content: str


# Test basic generation
print(claude.generate_text("hi."))

# Test structured generation
print(claude.generate_data("write a poem about a cat.", response_model=Poem))
