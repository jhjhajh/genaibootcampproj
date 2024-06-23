import streamlit as st
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.environ["OPENAI_API_KEY"]

def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state["history"] = []

    if "generated" not in st.session_state:
        st.session_state["generated"] = [
            "Hello! Feel free to ask me any questions."
        ]

    if "past" not in st.session_state:
        st.session_state["past"] = ["Hey! 👋"]

def conversation_chat(query, chain, history):
    result = chain({
        "question": query,
        "chat_history": history
    })
    history.append((query, result["answer"]))
    return result["answer"]

def display_chat_history(chain):
    user_input = st.chat_input("Type your question here")
    if user_input:
        with st.spinner("Generating response ......"):
            output = conversation_chat(
                query=user_input,
                chain=chain,
                history=st.session_state["history"]
            )

        st.session_state["past"].append(user_input)
        st.session_state["generated"].append(output)

    if st.session_state["generated"]:   
        for i in range(len(st.session_state["generated"])):
            with st.chat_message("user"):
                st.markdown(st.session_state["past"][i])
            with st.chat_message("assistant"):
                st.markdown(st.session_state["generated"][i])

def create_conversational_chain(vector_store):
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.1,
        openai_api_key=openai_api_key
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 2}),
        memory=memory
    )

    return chain

def main():
    initialize_session_state()
    st.title("ChatBot")
    st.sidebar.title("Document Processing")

    embedding = OpenAIEmbeddings()

    vector_store = Chroma(
        embedding_function=embedding,
        persist_directory="chroma_store"
    )

    chain = create_conversational_chain(vector_store=vector_store)
    display_chat_history(chain=chain)

if __name__ == "__main__":
    main()
