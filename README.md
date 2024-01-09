# Llama Chatbot

## Description
This project creates a conversational chatbot using the LLaMA 2 language model and deploys it as a web app using Streamlit.

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/llama-chatbot
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv env
    ```

3. **Activate the virtual environment:**
    - Windows:
      ```bash
      env\Scripts\activate
      ```
    - Linux/macOS:
      ```bash
      source env/bin/activate
      ```

4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Download Model
1. **Download the LLaMA 2 model:**
    ```bash
    cd llama-chatbot/models
    wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q8_0.bin
    ```

## Running the Chatbot
1. **Navigate to the project directory:**
    ```bash
    cd llama-chatbot
    ```

2. **Start the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

3. **Access the chatbot in your web browser:**
    - The app will usually open automatically in your default browser.
    - If not, the terminal will provide a URL (typically http://localhost:8501/) to access the app.

## Usage
1. Type your question or message in the input field.
2. Click the "Ask" button.
3. The chatbot will respond based on the LLaMA 2 model's understanding of your input.
4. Continue interacting with the chatbot as needed.
5. Type "bye" to end the conversation.

## Additional Notes
- The `handle_error` function provides basic error handling. Consider refining it for specific error cases and user-friendly responses.
- Explore Streamlit's layout and widget options for customizing the chatbot's visual appearance and interactivity.
