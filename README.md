# Portuguese AI Tutor 🇵🇹🤖

AI-powered Portuguese language learning platform with conversational practice.

## Features

- 🤖 **AI Chat Tutor** - Practice conversations with AI in Portuguese
- 📚 **Vocabulary Builder** - Track and practice new words
- 📖 **Grammar Lessons** - Interactive grammar explanations
- 🎯 **Personalized Practice** - AI adapts to your level
- 📊 **Progress Tracking** - Monitor your learning journey
- 🎤 **Speech Practice** (Coming soon) - Pronunciation feedback

## Quick Start

```bash
# Clone the repository
git clone https://github.com/rbtrends2/portuguese-ai-tutor.git
cd portuguese-ai-tutor

# Install dependencies
pip install -r requirements.txt

# Set up OpenAI API key
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# Run the chat interface
python src/chat_tutor.py
```

## Project Structure

```
portuguese-ai-tutor/
├── src/
│   ├── chat_tutor.py          # Main AI chat interface
│   ├── vocabulary_manager.py   # Vocabulary tracking
│   ├── grammar_engine.py       # Grammar lessons
│   └── progress_tracker.py     # Learning analytics
├── data/
│   ├── vocabulary/             # Vocabulary lists by topic
│   ├── grammar/                # Grammar lesson content
│   └── user_data/              # User progress (gitignored)
├── gui/
│   └── chat_interface.py       # PyQt6 GUI (optional)
├── tests/
│   └── test_chat_tutor.py
├── docs/
│   └── LEARNING_GUIDE.md
├── requirements.txt
├── .env.example
└── README.md
```

## Usage Examples

### Chat with AI Tutor

```python
from src.chat_tutor import PortugueseTutor

tutor = PortugueseTutor()
response = tutor.chat("Como se diz 'hello' em português?")
print(response)
# "Olá! 'Hello' em português é 'Olá' ou 'Oi' (informal)."
```

### Add Vocabulary

```python
from src.vocabulary_manager import VocabularyManager

vocab = VocabularyManager()
vocab.add_word("olá", "hello", category="greetings")
vocab.practice_session()
```

## Learning Paths

1. **Beginner** - Basic greetings, numbers, common phrases
2. **Intermediate** - Past/future tense, conversations, reading
3. **Advanced** - Subjunctive mood, idiomatic expressions, writing

## Technology Stack

- **AI**: OpenAI GPT-4 for conversational practice
- **GUI**: PyQt6 for desktop interface
- **Storage**: JSON for vocabulary/progress tracking
- **Future**: Speech recognition (Whisper API)

## Contributing

Contributions welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - See [LICENSE](LICENSE) for details.

## Roadmap

- [x] AI chat interface
- [ ] Vocabulary flashcards with spaced repetition
- [ ] Grammar quizzes
- [ ] Speech-to-text practice
- [ ] Mobile app (React Native)
- [ ] Gamification (points, streaks, achievements)
