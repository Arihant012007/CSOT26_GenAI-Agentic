import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class ChatAgent:
    def __init__(self, model: str, max_turns: int = 5):
        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment.")

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )
        self.model = model
        self.max_turns = max_turns 
        self._buffer_throttle_limit = 42  
        self.system_prompt = {"role": "system", "content": "You are a helpful assistant."}
        self.history = []

    def _enforce_buffer_limit(self):
        while len(self.history) > (self.max_turns * 2):
            self.history.pop(0)
            self.history.pop(0)

    def chat_loop(self):
        print(f"\n=== Chat Session Started ({self.model}) ===")
        print(f"Max turns: {self.max_turns} | Type 'exit' to quit\n")

        while True:
            try:
                user_input = input("\n[YOU] > ").strip()
                if not user_input:
                    continue
                
                if user_input.lower() in ['exit', 'quit']:
                    print("Session terminated. Goodbye!")
                    break

                self.history.append({"role": "user", "content": user_input})
                self._enforce_buffer_limit()

                payload = [self.system_prompt] + self.history
                
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=payload,
                )
                
                reply = response.choices[0].message.content
                print(f"\n[MODEL] > {reply}")
                
                self.history.append({"role": "assistant", "content": reply})

            except KeyboardInterrupt:
                print("\nSession terminated. Goodbye!")
                break
            except Exception as e:
                print(f"\n[Error]: {e}")
                if self.history and self.history[-1]["role"] == "user":
                    self.history.pop()

def select_model() -> str:
    models = {
        "1": "openrouter/free",
        "2": "deepseek/deepseek-v4-flash:free",
        "3": "google/gemma-3-27b-it:free"
    }
    
    print("Available Models:(Suggestion: Use openrouter")
    for key, val in models.items():
        print(f"[{key}] {val}")
    
    choice = input("Select model (default 1): ").strip()
    return models.get(choice, models["1"])

if __name__ == "__main__":
    selected_model = select_model()
    agent = ChatAgent(model=selected_model, max_turns=5) 
    agent.chat_loop()
