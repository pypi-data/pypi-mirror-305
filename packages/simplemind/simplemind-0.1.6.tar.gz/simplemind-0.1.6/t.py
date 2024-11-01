import simplemind as sm

from pydantic import BaseModel


claude = sm.Session(llm_provider="groq")
print(claude.generate_text("hi."))


class Poem(BaseModel):
    title: str
    content: str


print(claude.generate_data("write a poem about a cat.", response_model=Poem))
