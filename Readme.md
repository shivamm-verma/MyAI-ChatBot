# *MyAI Chat-bot*
This AI Chatbot uses `llama3-8b-8192` and can also  use other models and passes the given context to pass the question through groq api and get the answer with the given context.
Ask my [bot](#screenshots) about me, and it will provide you with an answer just as I would! 🙌🏼✨

<br>


### ➡️ *Ask my bot here!⤵️*
![Click Me]("Link")


### What it uses?
- Streamlit (For bringing Application to the user, beautifully)
- groq API (Most Fastest API)
- Python

### What it offers?
- Shivam Verma(me), Personal assistance.
- You can ask thing about me, my work and my hobbies.
- This will also give you my social handles and mail if asked.
- Responsive design, as deployed by streamlit.

---

### How to setup?

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Create a virtual environment:
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```
3. Install the required dependencies:
   ```py
   pip install -r requirements.txt
   ```
4. Set up Streamlit secrets:
   - Create a .streamlit directory in the root of your project.
   - Inside the .streamlit directory, create a secrets.toml file.
   - Add your Groq API key to the secrets.toml file:
    ```toml
    [secrets]
    GROQ_API_CHATBOT="yourGroqAPI"
    SHIVAM_CONTEXT="AddPrivateInfoHere"
    ```
5. Run the Streamlit app:
    ```sh
    streamlit run Chatbot.py
    ```
6. Access the app:
   - Open your web browser and go to http://localhost:8501.

---

### 📸Screenshots

Mobile
![Mobile](<Images/Stremalit chatbot prev.png>)

Laptop
![Laptop](Images/Preview1.jpeg)


### About this Repository

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/shivamm-verma/MyAI-ChatBot)
![GitHub Repo stars](https://img.shields.io/github/stars/shivamm-verma/MyAI-ChatBot)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/shivamm-verma/MyAI-ChatBot)