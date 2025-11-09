"""
Tests for Portuguese AI tutor.
"""

import pytest
from unittest.mock import Mock, patch
from src.chat_tutor import PortugueseTutor


def test_tutor_initialization():
    """Test tutor initializes correctly."""
    with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
        tutor = PortugueseTutor()
        assert tutor.user_level == "beginner"
        assert len(tutor.conversation_history) == 0


def test_conversation_history():
    """Test conversation history tracking."""
    with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
        tutor = PortugueseTutor()
        
        # Mock API response
        with patch.object(tutor.client.chat.completions, "create") as mock_create:
            mock_response = Mock()
            mock_response.choices = [Mock()]
            mock_response.choices[0].message.content = "Test response"
            mock_create.return_value = mock_response
            
            tutor.chat("Test message")
            
            assert len(tutor.conversation_history) == 2
            assert tutor.conversation_history[0]["role"] == "user"
            assert tutor.conversation_history[1]["role"] == "assistant"


def test_reset_conversation():
    """Test conversation reset."""
    with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
        tutor = PortugueseTutor()
        tutor.conversation_history = [{"role": "user", "content": "test"}]
        
        tutor.reset_conversation()
        
        assert len(tutor.conversation_history) == 0
