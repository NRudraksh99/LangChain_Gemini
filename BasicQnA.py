from langchain_google_genai import ChatGoogleGenerativeAI as ai
import streamlit as st
#use of this code requires a Google api key
#such a key can be generated from: https://aistudio.google.com/app/apikey
#generated api key has to be stored as an environment variable named GOOGLE_API_KEY
st.title("Basic QnA using LangChain and Google AI API")
p=st.sidebar.text_input("Have any questions? Type your queries here!",max_chars=500,key="p")

if p:
    llm = ai(model="gemini-pro")
    result=llm.invoke(p).content
    st.write(f"**Your Result:**:\n{result}")