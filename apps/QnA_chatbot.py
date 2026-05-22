import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
os.environ["GOOGLE_API_KEY"] = "AIzaSyCr2_Z5EKZi8j3ifaw0yFu0RsabSi-Y0V4"

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


st.title("🤖Askly - AI QnA Bot")
st.markdown("My QnA Bot with Langchain and Google Gemini !")

if "messages" not in st.session_state :
    st.session_state.messages = []
    
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    
    with st.chat_message(role):
        st.write(content)
    
query =st.chat_input("Ask anything ?")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res.content)
    st.session_state.messages.append({"role": "ai", "content": res.content})
    
