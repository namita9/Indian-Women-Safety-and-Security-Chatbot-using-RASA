# Features
- 💼 Women at the Workplace
- 🕵️ Cybercrime
- 👀 Eve Teasing
- 🚗 Safe Travel

# Technologies Used
- **Python**: The programming language used for development.
- **Rasa**: Powers natural language processing and dialogue management.
- **Flask**: Utilized for developing the web interface.
- **Pyttsx3**: Enables speech recognition and text-to-speech functionalities.



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

## Usage



```bash
# To train the model
rasa train

# To start the action server
rasa run actions

# To start the Rasa server with the user interface
rasa run -m models --enable-api --cors "*"

# To start the custom app
python app.py

