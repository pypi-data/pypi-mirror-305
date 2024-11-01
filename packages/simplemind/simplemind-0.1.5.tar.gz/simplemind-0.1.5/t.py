import simplemind as sm

from pydantic import BaseModel

# r = sm.generate_text("hi.", llm_provider="gemini")
# print(r)

# conv = sm.create_conversation(llm_provider="gemini")
# conv.add_message(role="user", text="hi.")

# r = conv.send()
# print(r)


class MyModel(BaseModel):
    name: str
    age: int


r = sm.generate_data("hi.", response_model=MyModel, llm_provider="gemini")
print(r)
