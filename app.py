import os 
import streamlit as st
import google.generativeai as gen_ai
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title='Gemini Chatbot',
    page_icon='🤖',
    layout='centered'
)

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

gen_ai.configure(api_key=GEMINI_API_KEY)
model = gen_ai.GenerativeModel('gemini-1.5-flash')

def translate_role_for_streamlit(user_role):
    if user_role == 'model':
        return 'assistant'
    else:
        return user_role
    

if 'chat_session' not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title('🤖 Gemini Chatbot')

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

user_prompt = st.chat_input('Ask anything ...')

if user_prompt:
    with st.chat_message('user'):
        st.markdown(user_prompt)

    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    with st.chat_message('assistant'):
        st.markdown(gemini_response.text)