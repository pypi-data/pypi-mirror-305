from pprint import pprint

import simplemind as sm
from pydantic import BaseModel


pprint(
    sm.generate_text(
        prompt="42??",
        llm_provider="ollama",
        llm_model="llama3.2",
    )
)
