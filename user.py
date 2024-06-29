import streamlit as st
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from auth import *
from config import *


def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state["history"] = []

    if "generated" not in st.session_state:
        st.session_state["generated"] = ["Hello! 👋 How can I help you?"]

    if "past" not in st.session_state:
        st.session_state["past"] = []

def conversation_chat(query, chain, history):
    result = chain.invoke({
        "query": query
    })
    history.append((query, result['result']))
    return result['result']

def display_chat_history(chain):
    user_input = st.chat_input("Type your question here")
    if user_input:
        fullprompt = user_input + SystemConstants.SYSTEM_MESSAGE
        with st.spinner("Generating response ......"):
            output = conversation_chat(
                query=fullprompt,
                chain=chain,
                history=st.session_state["history"]
            )
        
        st.session_state["past"].append(user_input)
        st.session_state["generated"].append(output)

    if st.session_state["generated"]:   
        for i in range(len(st.session_state["generated"])):
            with st.chat_message("assistant"):
                st.markdown(st.session_state["generated"][i])
            if i < len(st.session_state["past"]):
                with st.chat_message("user"):
                    st.markdown(st.session_state["past"][i])

def create_conversational_chain(vector_store):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = RetrievalQA.from_llm(
    retriever=vector_store.as_retriever(), llm=llm
    )
    return chain

def user(authenticator, name):
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name},")
    option = st.sidebar.selectbox( 
    'Scheme',
     ('retirement', 'healthcare'),
     placeholder= 'Please select a scheme',
     index=None
     )
    if option is None:
        st.sidebar.error("Please choose a scheme")
    else:
        st.sidebar.write(f"Selected: {option}")
        
        
    st.sidebar.success(UIConstants.CHATBOT_CONTEXT)
    st.sidebar.info(UIConstants.SUGGESTIONS)
    initialize_session_state()
    st.title("ChatBot")

    embedding = OpenAIEmbeddings()

    vector_store = Chroma(
        embedding_function=embedding,
        persist_directory=option
    )

    chain = create_conversational_chain(vector_store=vector_store)
    display_chat_history(chain=chain)