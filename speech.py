import speech_recognition as sr

# Create speech recognizer
recognizer = sr.Recognizer()

# 100 NLP responses
responses = {
    # Greetings
    "hello": "Hello! How can I help you?",
    "hi": "Hi! Nice to meet you.",
    "hey": "Hey! How can I assist you?",
    "good morning": "Good morning! Have a wonderful day.",
    "good afternoon": "Good afternoon! How can I help you?",
    "good evening": "Good evening! What can I do for you?",
    "good night": "Good night! Sleep well.",
    "how are you": "I am fine. Thank you for asking!",
    "how is your day": "My day is going great. Thank you!",
    "nice to meet you": "Nice to meet you too!",

    # Assistant
    "your name": "I am your Voice-to-Text NLP Assistant.",
    "who are you": "I am an NLP-based Voice-to-Text Assistant.",
    "what can you do": "I can listen to your voice, convert it into text and provide responses.",
    "how do you work": "I use speech recognition and NLP techniques to understand your voice.",
    "are you ai": "Yes, I am a simple AI-based NLP assistant.",
    "are you a robot": "I am a software-based virtual assistant.",
    "who created you": "I was created as a Python NLP project.",
    "do you understand me": "I can understand many simple spoken commands.",
    "can you help me": "Yes! I will try my best to help you.",
    "are you intelligent": "I use programmed NLP techniques to process your questions.",

    # NLP and AI
    "what is nlp": "NLP stands for Natural Language Processing.",
    "natural language processing": "Natural Language Processing helps computers understand human language.",
    "what is natural language processing": "NLP is a branch of AI that helps computers process and understand human language.",
    "what is artificial intelligence": "Artificial Intelligence enables computers to perform intelligent tasks.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning allows computers to learn patterns from data.",
    "what is deep learning": "Deep Learning is a part of machine learning based on neural networks.",
    "what is chatbot": "A chatbot is software that communicates with users using text or voice.",
    "what is speech recognition": "Speech recognition converts spoken language into text.",
    "what is voice recognition": "Voice recognition is technology that processes human speech.",

    # Python
    "what is python": "Python is a popular high-level programming language.",
    "python language": "Python is widely used for AI, NLP, data science and web development.",
    "what is programming": "Programming is the process of writing instructions for a computer.",
    "what is variable": "A variable stores a value in a program.",
    "what is function": "A function is a reusable block of code that performs a specific task.",
    "what is loop": "A loop repeats a block of code multiple times.",
    "what is list": "A list is a Python collection that can store multiple values.",
    "what is dictionary": "A dictionary stores data as key-value pairs.",
    "what is string": "A string is a sequence of characters.",
    "what is python used for": "Python is used for AI, NLP, automation, data science and software development.",

    # Education
    "what is education": "Education is the process of gaining knowledge and skills.",
    "why is education important": "Education helps people develop knowledge, skills and confidence.",
    "what is engineering": "Engineering applies science and mathematics to solve real-world problems.",
    "what is computer science": "Computer Science is the study of computers, algorithms and software.",
    "what is electronics": "Electronics deals with electrical circuits and electronic components.",
    "what is iot": "IoT stands for Internet of Things, where devices communicate through networks.",
    "what is data science": "Data Science uses data, statistics and programming to find useful insights.",
    "what is data analytics": "Data Analytics involves examining data to discover useful information.",
    "what is software": "Software is a collection of programs that tells a computer what to do.",
    "what is hardware": "Hardware refers to the physical components of a computer.",

    # General knowledge
    "what is india": "India is a country in South Asia.",
    "capital of india": "The capital of India is New Delhi.",
    "what is earth": "Earth is the third planet from the Sun.",
    "what is moon": "The Moon is Earth's natural satellite.",
    "what is sun": "The Sun is the star at the center of our solar system.",
    "how many planets": "There are eight recognized planets in our solar system.",
    "largest planet": "Jupiter is the largest planet in our solar system.",
    "smallest planet": "Mercury is the smallest planet in our solar system.",
    "what is water": "Water is a chemical compound made of hydrogen and oxygen.",
    "what is oxygen": "Oxygen is an essential element needed by humans and many living organisms.",

    # Technology
    "what is computer": "A computer is an electronic device that processes data.",
    "what is internet": "The Internet is a global network connecting computers and devices.",
    "what is website": "A website is a collection of web pages available on the Internet.",
    "what is app": "An app is software designed to perform specific tasks.",
    "what is google": "Google provides Internet search and many other technology services.",
    "what is github": "GitHub is a platform used to store and collaborate on software projects.",
    "what is database": "A database is an organized collection of information.",
    "what is cloud computing": "Cloud computing provides computing resources over the Internet.",
    "what is cybersecurity": "Cybersecurity protects computers, networks and data from digital threats.",
    "what is automation": "Automation uses technology to perform tasks with minimal human intervention.",

    # Science
    "what is science": "Science is the systematic study of the natural world.",
    "what is physics": "Physics studies matter, energy, motion and their interactions.",
    "what is chemistry": "Chemistry studies substances, their properties and reactions.",
    "what is biology": "Biology is the study of living organisms.",
    "what is gravity": "Gravity is the force that attracts objects toward each other.",
    "what is electricity": "Electricity is associated with the movement of electric charge.",
    "what is energy": "Energy is the capacity to do work.",
    "what is solar energy": "Solar energy is energy obtained from sunlight.",
    "what is renewable energy": "Renewable energy comes from naturally replenishing sources.",
    "what is environment": "The environment includes natural surroundings and living systems.",

    # Conversation
    "what are you doing": "I am waiting for your next question.",
    "are you busy": "No, I am always ready to help.",
    "do you like me": "I am happy to assist you!",
    "tell me something": "Learning something new every day is a great habit.",
    "tell me a fact": "The Earth revolves around the Sun.",
    "give me motivation": "Believe in yourself and keep learning every day.",
    "i am happy": "That's wonderful! Keep smiling.",
    "i am sad": "I am sorry to hear that. I hope things get better soon.",
    "i am tired": "Take a short break and get some rest.",
    "i am bored": "Try learning something new or working on a creative project.",

    # Closing
    "thank you": "You're welcome!",
    "thanks": "You're very welcome!",
    "thank you so much": "It is my pleasure to help you!",
    "okay": "Okay! What would you like to know?",
    "ok": "Sure!",
    "great": "That's great!",
    "awesome": "Awesome! Keep going!",
    "bye": "Goodbye! Have a nice day!",
    "see you": "See you again! Take care.",
    "goodbye": "Goodbye! Thank you for using the assistant."
}


# NLP processing function
def process_text(text):
    text = text.lower().strip()

    # First check exact question
    if text in responses:
        return responses[text]

    # Then check keywords
    for keyword, response in responses.items():
        if keyword in text:
            return response

    return "Sorry, I don't understand that."


# Voice assistant function
def voice_assistant():

    print("=" * 50)
    print("       VOICE-TO-TEXT NLP ASSISTANT")
    print("=" * 50)
    print("Speak something...")
    print("Say 'exit' or 'quit' to stop.")

    while True:

        try:
            with sr.Microphone() as source:

                print("\nListening...")

                # Reduce background noise
                recognizer.adjust_for_ambient_noise(
                    source, duration=1
                )

                # Listen to user
                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=10
                )

            print("Recognizing...")

            # Convert voice to text
            text = recognizer.recognize_google(audio)

            print("You:", text)

            # Exit command
            if text.lower().strip() in ["exit", "quit", "goodbye"]:
                print("Assistant: Goodbye!")
                break

            # NLP response
            answer = process_text(text)

            print("Assistant:", answer)

        except sr.WaitTimeoutError:
            print("Assistant: No speech detected.")

        except sr.UnknownValueError:
            print("Assistant: Sorry, I could not understand your voice.")

        except sr.RequestError:
            print("Assistant: Speech recognition service is unavailable.")

        except OSError:
            print("Assistant: Microphone not found.")
            break


# Start the assistant
if __name__ == "__main__":
    voice_assistant()