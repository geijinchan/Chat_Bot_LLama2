# Import necessary libraries
import streamlit as st  # Streamlit for web app development
from langchain.prompts import PromptTemplate  # Prompt engineering
from langchain.llms import CTransformers  # Loading and interacting with language models

# Function to generate a response from the LLaMA 2 model
def getLLamaResponse(question):
    """
    Generates a response from the LLaMA 2 model given a question.

    Args:
        question (str): The question to be answered by the model.

    Returns:
        str: The generated response from the model.
    """

    model = CTransformers(
        model='llama-2-7b-chat.ggmlv3.q8_0.bin',  # Load the LLaMA 2 model
        model_type='llama',
        config={
            'max_new_tokens': 256,  # Set maximum length of generated response
            'temperature': 0.9  # Adjust creativity and randomness in responses
        }
    )
    response = model.invoke(question)  # Generate the response using the model
    return response

# Function to display chatbot greetings and initial messages
def greet_user():
    """
    Greets the user and introduces the chatbot.
    """

    st.title("Llama Chatbot")  # Set the page title
    st.write("Hello there! I am Llama 2, an LLM, and I will be your chatbot today. Ask me anything!")

# Function to handle errors gracefully
def handle_error(error):
    """
    Handles exceptions that occur during chatbot interactions.

    Args:
        error: The exception that was raised.
    """

    print(error)  # Print the exception for debugging purposes
    st.warning("I'm not sure I understand. Could you please rephrase your question?")

# Main function to control the chatbot's logic and user interactions
def main():
    """
    Coordinates the overall logic and flow of the chatbot application.
    """

    greet_user()  # Greet the user

    # Create an input field for user questions
    user_input = st.text_input("You:", key="user_input")

    # Ask button
    if st.button("Ask"):
        try:
            st.text("You: " + user_input)  # Display the user's question

            if user_input.lower() == "bye":
                st.text("Chatbot: It was nice chatting with you! See you next time.")
            elif user_input.lower() in ["hi", "hello", "hey"]:
                st.text("Chatbot: Hello there again! How can I help you further?")
            else:
                response = getLLamaResponse(user_input)  # Get the model's response
                st.text("Chatbot: " + response)  # Display the model's response

            st.text_input("You:", value="", key="user_input")  # Clear the input field

        except Exception as e:
            handle_error(e)  # Handle any exceptions that occur

if __name__ == "__main__":
    main()
