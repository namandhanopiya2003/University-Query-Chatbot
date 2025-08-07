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

university_chatbot/<br>
│<br>
├── data/<br>
│   ├── intents.json                    # Intent definitions (tags, patterns, responses, context)<br>
│   ├── entities.json                   # Entity definitions (optional for slot-filling)<br>
│   └── knowledge_base.json             # Static FAQs or university info (optional)<br>
│<br>
├── chatbot/<br>
│   ├── __init__.py<br>
│   ├── preprocess.py                   # Loading & preprocessing data<br>
│   ├── model.py                        # Training & loading intent classification model<br>
│   ├── intent_classifier.py            # Predict intent & confidence scores<br>
│   ├── entity_extractor.py             # Extract entities from user input (dates, courses, etc.)<br>
│   ├── context_manager.py              # Manage user session contexts & conversation states<br>
│   ├── dialogue_manager.py             # Decide next bot action based on intent, context, entities<br>
│   ├── responder.py                    # Generate responses (templated or dynamic)<br>
│   ├── utils.py                        # Helper functions (e.g., text cleaning, random response selection)<br>
│   └── logger.py                       # Log conversations for analysis/improvements<br>
│<br>
├── tests/                              # Unit tests for modules (optional but recommended)<br>
│   ├── test_intent_classifier.py<br>
│   ├── test_context_manager.py<br>
│   └── test_responder.py<br>
│<br>
├── venv/<br>
│<br>
├── chatbot.log<br>
├── main.py                             # Chatbot terminal interface<br>
├── requirements.txt                    # Python package dependencies<br>
├── README.md                           # Setup and usage instructions<br>
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

## ✨ SAMPLE OUTPUT ==>

💬 You: "Hi, can you tell me the admission process?"<br>
🤖 Chatbot: "Sure! You can visit the official admission page for full details."<br>

💬 You: "What events are conducted in college?"<br>
🤖 Chatbot: "For event details, visit 'here' "<br>

💬 You: "quit"<br>
🤖 Chatbot: "Goodbye! Have a nice day."<br>

🟢 Status: User query successfully classified with high confidence.

---

## 📬 CONTACT ==>

For questions or feedback, feel free to reach out!


---


