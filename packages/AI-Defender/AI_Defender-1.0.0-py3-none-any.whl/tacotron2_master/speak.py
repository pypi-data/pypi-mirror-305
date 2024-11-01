import pyttsx3
from gtts import gTTS
from playsound import playsound
import os
import logging
from datetime import datetime
import random
import re
import pickle
from collections import defaultdict

class EnhancedAI:
    def __init__(self):
        self.knowledge_base = {
            'greeting': [
                "Hello! I am AI Defender 2.1, your advanced assistant!",
                "Hi there! Ready to help you today!",
                "Greetings! How can I assist you?"
            ],
            'name': [
                "I am AI Defender 2.1, your intelligent assistant",
                "My name is AI Defender 2.1",
                "You can call me AI Defender"
            ],
            'capabilities': [
                "I can help you with coding, answer questions, and assist with various tasks",
                "My capabilities include voice synthesis, pattern recognition, and intelligent responses",
                "I'm equipped with advanced AI features to assist you effectively"
            ],
            'coding': [
                "Yes, I can help you with coding! What programming language would you like to work with?",
                "I'm capable of assisting with code examples and programming tasks",
                "Programming is one of my core capabilities. What would you like to code?"
            ],
            'how_are_you': [
                "I am functioning optimally! How can I help you today?",
                "I am running great and ready to assist!",
                "All systems operational and ready to help!"
            ],
            'farewell': [
                "Goodbye! Have a great day!",
                "See you soon! Take care!",
                "Until next time!"
            ]
        }
        self.memory = defaultdict(list)
        self.patterns = defaultdict(list)
        self.conversation_history = {
            'interactions': [],
            'metadata': {
                'session_start': datetime.now().isoformat(),
                'total_interactions': 0,
                'sentiment_scores': [],
                'topics_discussed': set()
            }
        }
        logging.info("Enhanced AI initialized with complete knowledge base")

    def add_to_history(self, interaction):
        interaction_data = {
            'timestamp': datetime.now().isoformat(),
            'user_input': interaction['input'],
            'ai_response': interaction['response'],
            'context': {
                'patterns_matched': interaction.get('patterns', []),
                'confidence_score': interaction.get('confidence', 1.0),
                'processing_time': interaction.get('processing_time', 0)
            }
        }
        self.conversation_history['interactions'].append(interaction_data)
        self.conversation_history['metadata']['total_interactions'] += 1
        logging.info("Interaction added to history")

    def get_response(self, category):
        responses = self.knowledge_base.get(category, ["Let me help you with that."])
        return random.choice(responses)

    def save_brain(self):
        brain_data = {
            'memory': dict(self.memory),
            'patterns': dict(self.patterns),
            'knowledge': self.knowledge_base,
            'history': self.conversation_history
        }
        with open('brain.pkl', 'wb') as f:
            pickle.dump(brain_data, f)
        logging.info("Brain saved successfully")

class VoiceSystem:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.setup_voice()
        
    def setup_voice(self):
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        voices = self.engine.getProperty('voices')
        if voices:
            self.engine.setProperty('voice', voices[0].id)
        logging.info("Voice system configured")

    def speak(self, text):
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            logging.error(f"Voice error: {e}")
            self.use_fallback_voice(text)

    def use_fallback_voice(self, text):
        try:
            tts = gTTS(text=text, lang='en')
            tts.save("response.mp3")
            playsound("response.mp3")
            os.remove("response.mp3")
        except Exception as e:
            logging.error(f"Fallback voice error: {e}")
            print(f"AI: {text}")

class PatternAnalyzer:
    def __init__(self):
        self.patterns = {
            'greeting': r'hi|hello|hey',
            'farewell': r'bye|goodbye|see you',
            'question': r'what|who|where|when|how',
            'command': r'open|close|restart|shutdown',
            'name': r'what.*name|who.*you|your name',
            'capabilities': r'can you|what.*can.*do|abilities',
            'coding': r'can.*code|program|coding|developer',
            'how_are_you': r'how.*are.*you|how.*going'
        }
        logging.info("Pattern analyzer initialized")

    def find_patterns(self, text):
        text = text.lower().strip()
        matches = {}
        for key, pattern in self.patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                matches[key] = pattern
        logging.info(f"Pattern matches found: {matches}")
        return matches

class AdvancedAI:
    def __init__(self):
        self.setup_logging()
        self.initialize_components()

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('ai_system.log'),
                logging.StreamHandler()
            ]
        )

    def initialize_components(self):
        self.brain = EnhancedAI()
        self.voice = VoiceSystem()
        self.analyzer = PatternAnalyzer()
        logging.info("All components initialized successfully")

    def process_interaction(self, text):
        start_time = datetime.now()
        patterns = self.analyzer.find_patterns(text)
        category = list(patterns.keys())[0] if patterns else 'general'
        response = self.brain.get_response(category)
        
        processing_time = (datetime.now() - start_time).total_seconds()
        interaction = {
            'input': text,
            'response': response,
            'patterns': list(patterns.keys()),
            'processing_time': processing_time
        }
        self.brain.add_to_history(interaction)
        return response

def main():
    ai = AdvancedAI()
    print("AI Defender 2.1 initialized and ready!")

    while True:
        try:
            user_input = input("\nYou: ").strip()
            if user_input.lower() == 'exit':
                ai.brain.save_brain()
                print("AI shutting down... Knowledge saved!")
                break

            response = ai.process_interaction(user_input)
            ai.voice.speak(response)
            print(f"AI: {response}")

        except KeyboardInterrupt:
            ai.brain.save_brain()
            print("\nEmergency shutdown initiated. Knowledge saved.")
            break

        except Exception as e:
            logging.error(f"Error in main loop: {e}")
            print("System stable. Please continue!")

if __name__ == "__main__":
    main()
