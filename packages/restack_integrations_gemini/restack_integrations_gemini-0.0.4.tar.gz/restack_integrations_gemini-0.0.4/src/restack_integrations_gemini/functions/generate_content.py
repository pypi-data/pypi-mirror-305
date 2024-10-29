from pydantic import BaseModel
import google.generativeai as genai

class GeminiGenerateContentInput(BaseModel):
    user_content: str
    model: str | None = None
    api_key: str = ""

def gemini_generate_content(input) :
    if not input.api_key:
        raise ValueError("api_key is required")
    
    genai.configure(api_key=input.api_key)

    model = genai.GenerativeModel(model_name=input.model)

    response = model.generate_content(input.user_content)

    return response.text

# if __name__ == "__main__":

#     test_inputs = [
#         GeminiGenerateContentInput(
#             user_content="The opposit of love is",
#             model="gemini-1.5-flash",
#             api_key="AIzaSyCpDdalMfFCwf6Ix1iDzVY5_HaJLYFdDcU",
#         ),
#         GeminiGenerateContentInput(
#             user_content="The opposite of hot is",
#             model="gemini-1.5-flash",
#             api_key="AIzaSyCpDdalMfFCwf6Ix1iDzVY5_HaJLYFdDcU",
#         ),
#     ]

#     def run_tests():
#         for i, input in enumerate(test_inputs, 1):
#             print(f"\nTest {i}:")
#             print(f"Input: {input}")
#             result = gemini_generate_content(input)
#             print(f"Response: {result}")
#             print("-" * 50)

#     run_tests()

