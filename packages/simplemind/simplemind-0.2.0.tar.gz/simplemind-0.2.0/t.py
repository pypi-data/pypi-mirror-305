import simplemind as sm
from pydantic import BaseModel


class InstructionStep(BaseModel):
    step_number: int
    instruction: str


class RecipeIngredient(BaseModel):
    name: str
    quantity: float
    unit: str


class Recipe(BaseModel):
    name: str
    ingredients: list[RecipeIngredient]
    instructions: list[InstructionStep]


recipe = sm.generate_data(
    "Write a recipe for chocolate chip cookies",
    llm_model="gpt-4o-mini",
    llm_provider="openai",
    response_model=Recipe,
)
