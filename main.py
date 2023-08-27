import streamlit as st
from langchain.chat_models import ChatOpenAI


#streamlit title
st.title('This is a :green[chatGPT] by :blue[Python]')

#streamlit input
text = st.text_input('Question?')

#chatGPT answer
chat_model = ChatOpenAI()

result = chat_model.predict(text)

#button
if st.button('Send'):
    st.write(result)