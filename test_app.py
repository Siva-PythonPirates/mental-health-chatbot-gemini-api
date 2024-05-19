import os
import streamlit as st
import google.generativeai as genai

# Initialize the Gemini-Pro model
os.environ['GOOGLE_GEMINI_KEY'] = "AIzaSyBoVQYDOeYH8L4-GZRL6b82nJAZJSESi-A"
genai.configure(api_key=os.getenv('GOOGLE_GEMINI_KEY'))
model = genai.GenerativeModel('gemini-pro')


# Define a function to send the user's message to the model and get the response
def get_model_response(user_input):
    prompt = "act as a professional mental health therapist answer my query with your best possible response..."
    response = model.generate_content(user_input)
    return response.text

# Define a function to convert the role of the message to a Streamlit chat message role
def role_to_streamlit(role):
    return "Therapistia" if role == "Bot" else "User"

# Display the chat interface
def main():
    st.title("Mental Health Counselor Chat")
    
    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Display user input box and send button
    user_input = st.text_input("You: ", key="user_input")
    if st.button("Send"):
        st.session_state.chat_history.append(("user", user_input))
        bot_response = get_model_response(user_input)
        st.session_state.chat_history.append(("Bot", bot_response))
    
    # Display chat history
    if st.session_state.chat_history:
        for role, message in st.session_state.chat_history:
            st.write(f"{role_to_streamlit(role)}: {message}")

    # Adjust layout
    st.markdown(""" 
        <style> 
        .stTextInput>div>div {
            width: 70%;
        }
        .stText>div {
            text-align: left;
        }
        </style>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
