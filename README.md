# Indian-Women-Safety-and-Security-Chatbot-using-RASA
 The Women's Safety Chatbot is an AI-driven assistant providing guidance on cybercrime, occupational safety, public harassment, and safe travel for women. Utilizing Flask, Pyttsx3, and Rasa, it offers reliable information to help women make informed decisions and stay safe.
# Technologies Used
Rasa: For natural language processing and dialogue management.
Flask: For developing the web interface.
Pyttsx3: For speech recognition and text-to-speech functionalities.

## Installation

1. **Prerequisites**:
    - Python 3.6-3.8
    - pip (Python package installer)
    - Virtual environment tool (optional but recommended)
    - Rasa framework 3.1.1
    - Flask
    - SpeechRecognition
    - gtts
    - Pttys3x
    - spaCy and its language model (optional for better NLP performance)

2. **Steps**:
    ```bash
    # Clone the repository
    git clone https://github.com/yourusername/projectname.git

    # Navigate to the project directory
    cd projectname

    # Create a virtual environment (optional but recommended)
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

    # Install dependencies
    pip install -r requirements.txt

    # Install Rasa
    pip install rasa

    # Install spaCy and its language model (optional)
    pip install -U spacy
    python -m spacy download en_core_web_md

    # (Optional) Link spaCy model to Rasa
    python -m spacy link en_core_web_md en
    ```



## Usage

Provide examples and instructions on how to use your project.

```bash
# To train the model
rasa train

# To start the action server
rasa run actions

# To start the Rasa server with the user interface
rasa run -m models --enable-api --cors "*"

# To start the custom app
python app.py
