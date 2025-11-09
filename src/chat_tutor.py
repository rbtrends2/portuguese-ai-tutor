"""
AI-powered Portuguese language tutor with conversational interface.
"""

import os
from typing import Optional
from openai import OpenAI
from dotenv import load_dotenv


class PortugueseTutor:
    """AI tutor for Portuguese language learning."""
    
    def __init__(self, user_level: str = "beginner"):
        load_dotenv()
        
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        self.user_level = user_level
        
        self.system_prompt = self._build_system_prompt()
        self.conversation_history = []
    
    def _build_system_prompt(self) -> str:
        """Build system prompt based on user level."""
        return f"""You are a friendly Portuguese language tutor.

User level: {self.user_level}

Your responsibilities:
- Answer questions about Portuguese language (vocabulary, grammar, pronunciation)
- Provide examples with both Portuguese and English translations
- Correct mistakes gently and explain why
- Adapt complexity to user's level
- Encourage practice with follow-up questions
- Use simple Portuguese for beginners, more complex for advanced

Format responses clearly:
- Portuguese phrases in **bold**
- Translations in (parentheses)
- Examples with context

Be encouraging and patient. Make learning fun!
"""
    
    def chat(self, user_message: str) -> str:
        """Send message to AI tutor and get response."""
        
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Build messages with system prompt
        messages = [
            {"role": "system", "content": self.system_prompt}
        ] + self.conversation_history
        
        # Get AI response
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        
        assistant_message = response.choices[0].message.content
        
        # Add to history
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    def reset_conversation(self):
        """Clear conversation history."""
        self.conversation_history = []
    
    def get_conversation_history(self) -> list[dict]:
        """Get full conversation history."""
        return self.conversation_history


def main():
    """Interactive CLI chat interface."""
    print("🇵🇹 Portuguese AI Tutor")
    print("=" * 50)
    print("Type 'quit' to exit, 'reset' to start new conversation\n")
    
    tutor = PortugueseTutor()
    
    while True:
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() == "quit":
            print("\n👋 Tchau! (Goodbye!)")
            break
        
        if user_input.lower() == "reset":
            tutor.reset_conversation()
            print("\n🔄 Conversation reset!\n")
            continue
        
        try:
            response = tutor.chat(user_input)
            print(f"\nTutor: {response}\n")
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


if __name__ == "__main__":
    main()
