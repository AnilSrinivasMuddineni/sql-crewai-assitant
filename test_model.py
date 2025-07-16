from crewai import LLM
from openai import BaseModel

class Dog(BaseModel):
    name: str
    age: int
    breed: str


llm = LLM(model="gpt-4o",
          api_key="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", 
          response_format=Dog)

response = llm.call(
    "Analyze the following messages and return the name, age, and breed. "
    "Meet Kona! She is 3 years old and is a black german shepherd."
)
print(response)

# Output:
# Dog(name='Kona', age=3, breed='black german shepherd')