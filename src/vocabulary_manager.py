"""
Vocabulary tracking and practice system.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Optional


class VocabularyManager:
    """Manage vocabulary lists and practice sessions."""
    
    def __init__(self, data_dir: str = "data/user_data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.vocab_file = self.data_dir / "vocabulary.json"
        
        self.vocabulary = self._load_vocabulary()
    
    def _load_vocabulary(self) -> dict:
        """Load vocabulary from file."""
        if self.vocab_file.exists():
            return json.loads(self.vocab_file.read_text(encoding="utf-8"))
        return {"words": [], "categories": {}}
    
    def _save_vocabulary(self):
        """Save vocabulary to file."""
        self.vocab_file.write_text(
            json.dumps(self.vocabulary, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
    
    def add_word(
        self,
        portuguese: str,
        english: str,
        category: str = "general",
        example: Optional[str] = None
    ):
        """Add new word to vocabulary."""
        
        word_entry = {
            "portuguese": portuguese,
            "english": english,
            "category": category,
            "example": example,
            "added_date": datetime.now().isoformat(),
            "practice_count": 0,
            "correct_count": 0
        }
        
        self.vocabulary["words"].append(word_entry)
        
        # Update category index
        if category not in self.vocabulary["categories"]:
            self.vocabulary["categories"][category] = []
        self.vocabulary["categories"][category].append(portuguese)
        
        self._save_vocabulary()
        print(f"✅ Added: {portuguese} = {english}")
    
    def get_words_by_category(self, category: str) -> list[dict]:
        """Get all words in a category."""
        return [
            w for w in self.vocabulary["words"]
            if w["category"] == category
        ]
    
    def practice_session(self, category: Optional[str] = None):
        """Start a practice session."""
        words = (
            self.get_words_by_category(category)
            if category
            else self.vocabulary["words"]
        )
        
        if not words:
            print("No words to practice!")
            return
        
        print(f"\n📚 Practice Session - {len(words)} words\n")
        
        correct = 0
        for word in words:
            print(f"Portuguese: {word['portuguese']}")
            answer = input("English: ").strip().lower()
            
            if answer == word["english"].lower():
                print("✅ Correct!\n")
                correct += 1
                word["correct_count"] += 1
            else:
                print(f"❌ Wrong. Answer: {word['english']}\n")
            
            word["practice_count"] += 1
        
        self._save_vocabulary()
        
        score = (correct / len(words)) * 100
        print(f"\n🎯 Score: {correct}/{len(words)} ({score:.1f}%)")


def main():
    """Demo vocabulary manager."""
    vocab = VocabularyManager()
    
    # Add sample words
    vocab.add_word("olá", "hello", "greetings", "Olá! Como vai?")
    vocab.add_word("obrigado", "thank you", "greetings", "Obrigado pela ajuda!")
    vocab.add_word("tchau", "bye", "greetings", "Tchau! Até logo!")
    
    # Practice
    vocab.practice_session("greetings")


if __name__ == "__main__":
    main()
