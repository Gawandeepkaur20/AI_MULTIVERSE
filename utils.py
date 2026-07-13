

import streamlit as st
from config import TOKEN_RATIO




def initialize_session():
    """
    Initialize session state variables.
    """

    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    if "conversation_log" not in st.session_state:
        st.session_state.conversation_log = []    

    if "total_characters" not in st.session_state:
        st.session_state.total_characters = 0

    if "total_words" not in st.session_state:
        st.session_state.total_words = 0

    if "total_tokens" not in st.session_state:
        st.session_state.total_tokens = 0




def add_user_message(message):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    st.session_state.conversation_log.append(
        {
            "role": "user",
            "content": message,
            "personality": st.session_state.selected_personality
        }
    )

def add_ai_message(message):

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": message
        }
    )

    st.session_state.conversation_log.append(
        {
            "role": "assistant",
            "content": message,
            "personality": st.session_state.selected_personality
        }
    )
    

def clear_chat():
    """
    Clear complete conversation.
    """

    st.session_state.messages = []
    
    st.session_state.conversation_log = []

    st.session_state.total_characters = 0

    st.session_state.total_words = 0

    st.session_state.total_tokens = 0



def count_characters(text):

    return len(text)


def count_words(text):

    return len(text.split())


def estimate_tokens(text):

    return round(len(text) / TOKEN_RATIO)



def update_statistics(text):

    st.session_state.total_characters += count_characters(text)

    st.session_state.total_words += count_words(text)

    st.session_state.total_tokens += estimate_tokens(text)



def display_chat():

    for message in st.session_state.conversation_log:

        if message["role"] == "user":

            with st.chat_message("user"):

                st.write(message["content"])

        else:

            with st.chat_message("assistant"):

                st.write(message["content"])



def build_conversation():

    history = ""

    for message in st.session_state.messages:

        if message["role"] == "user":

            history += f"User: {message['content']}\n"

        else:

            history += f"Assistant: {message['content']}\n"

    return history
