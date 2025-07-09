## UNIVERSITY_QUERY_CHATBOT

## 🧠 ABOUT THIS PROJECT ==>

- This is a Python-based chatbot system that answers university-related queries using Natural Language Processing (NLP) and Machine Learning.

- The chatbot learns from a structured JSON file containing intents (like events, admission, hostel, etc.), patterns (user input examples), and responses.

- It uses Logistic Regression for intent classification and CountVectorizer for text vectorization.

- This project is ideal for college websites, academic demonstrations, or integrating with virtual assistants.

- This chatbot works like a rule-based + intent classification chatbot:
--> Uses TF-IDF Vectorizer to convert text into numbers.
--> A classifier model (like SVM, Naive Bayes, etc.) predicts the intent.
--> Based on the intent, it gives a predefined response from intents.json.
--> Confidence threshold is used to decide if the bot “understands” the user.

---

## ⚙ TECHNOLOGIES USED ==>

- **Python**

- **NLTK** (for tokenization and preprocessing)

- **Scikit-learn** (for vectorization, label encoding, and model training)

- **NumPy**

- **Joblib** (for saving the model, vectorizer, and encoders)

---

## 📁 PROJECT FOLDER STRUCTURE ==>

university_chatbot/
│
├── data/
│   ├── intents.json                    # Intent definitions (tags, patterns, responses, context)
│   ├── entities.json                   # Entity definitions (optional for slot-filling)
│   └── knowledge_base.json             # Static FAQs or university info (optional)
│
├── chatbot/
│   ├── __init__.py
│   ├── preprocess.py                   # Loading & preprocessing data
│   ├── model.py                        # Training & loading intent classification model
│   ├── intent_classifier.py            # Predict intent & confidence scores
│   ├── entity_extractor.py             # Extract entities from user input (dates, courses, etc.)
│   ├── context_manager.py              # Manage user session contexts & conversation states
│   ├── dialogue_manager.py             # Decide next bot action based on intent, context, entities
│   ├── responder.py                    # Generate responses (templated or dynamic)
│   ├── utils.py                        # Helper functions (e.g., text cleaning, random response selection)
│   └── logger.py                       # Log conversations for analysis/improvements
│
├── tests/                              # Unit tests for modules (optional but recommended)
│   ├── test_intent_classifier.py
│   ├── test_context_manager.py
│   └── test_responder.py
│
├── venv/
│
├── chatbot.log
├── main.py                             # Chatbot terminal interface
├── requirements.txt                    # Python package dependencies
├── README.md                           # Setup and usage instructions
└── config.yaml                         # Configuration parameters (model paths, thresholds, etc.)

---

## 📝 WHAT EACH FILE DOES ==>

**`data/intents.json`**
- Contains all the defined intents for the chatbot. Each intent has:
- tag: category of the intent (e.g., admission, events)
- patterns: possible user inputs
- responses: bot's replies

**`main.py`**
- Loads the trained model and NLP tools.
- Takes user input and predicts intent.
- Selects and returns an appropriate response.

**`train_model.py`**
- Reads the intents.json.
- Converts patterns into vectors using CountVectorizer.
- Trains a Logistic Regression classifier.
- Saves the trained model, vectorizer, and label encoder.

**`chatbot/`**
- Contains all saved machine learning components for reuse.

**`requirements.txt`**
- Lists all necessary Python packages:

---

## 🚀 HOW TO RUN ==>

- Open cmd and run following commands ->

# Step 1: Move to the project directory:
cd "D:\CHATBOT"
D:

# Step 2: Create a virtual machine:
python -m venv venv

# Step 3: Run virtual machine:
venv\Scripts\activate

# Step 4: Install all necessary python packages:
pip install -r requirements.txt

# Step 5: Train the chatbot model:
python chatbot/train_model.py

# Step 6: Run the chatbot model:
python main.py

---

## ✅ IMPROVEMENTS MADE ==>

- Implemented model persistence using Joblib for reusability without retraining every time.

- Structured code for clarity, separating training logic, intent prediction, and chatbot response flow.

- Enhanced intent recognition accuracy by preprocessing text and optimizing vectorization.

- Integrated confidence thresholding to reduce false matches and improve response reliability.

- Expanded intent coverage by generating over 1000 diverse university-related tags and patterns.

- Built flexible response system using JSON, allowing easy updates to responses and patterns without touching the core code.

---

## 📌 To Do / Future Enhancements ==>

- Add GUI or Web-based interface.

- Connect to university database or live API.

- Integrate voice-based interaction.

---

## ✨ SAMPLE OUTPUT ==>

💬 You: "Hi, can you tell me the admission process?"
🤖 Chatbot: "Sure! You can visit the official admission page for full details."

💬 You: "What events are conducted in college?"
🤖 Chatbot: "For event details, visit <a target="_blank" href="ADD YOUR FUNCTIONS LINK OR YOUR OWN RESPONSE"> here</a>"

💬 You: "quit"
🤖 Chatbot: "Goodbye! Have a nice day."

🟢 Status: User query successfully classified with high confidence.

---

## 📬 CONTACT ==>

For questions or feedback, feel free to reach out!

---